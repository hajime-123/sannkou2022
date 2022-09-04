using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Threading;
using System.Threading.Tasks;
using System.IO;
using System.Net;

namespace PLCPCconnectionTool
{


    public partial class frmMain : Form
    {
        // ロード時、最小化フラグ
        public static Boolean gbolLoadFormMinimum = false;

        // INIファイルから取得するグローバル変数
        public static String gstrPLC_IP;
        public static Int32 gintPort;
        public static String gstrLOGpath;
        public static String gstrPassWord;
        public static String gstrLOGfilename;
        public static Int32 gintLOGtimeInfo;
        public static Int32 gintLOGsaveLength;
        public static Boolean gbolLOGtimeLoc;
        public static Boolean gbolLOGdelAuto;
        public static Int32 gintStartDelay;
        public static Boolean gbolDelayOn;

        // ログファイルに使用するタイムスタンプ
        public string gstrFileTimeStamp = "";

        // ログファイルパス
        string gstrfilePath = "";

        // LANクラス
        EthernetComm LAN = new EthernetComm();

        // LAN接続中フラグ
        public Boolean gbolConnection=false;


        public frmMain()
        {
            InitializeComponent();
        }

        private void timGetTime_Tick(object sender, EventArgs e)
        {
            // 1秒間隔で更新
            lblTimeNow.Text = DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss");
        }

        private bool funIniLoadAndSet()
        {
            try
            {
                // INIファイルの取得

                string[] lines1;
                string line;
                string[] rows;

                lines1 = System.IO.File.ReadAllLines(GlbSetVal.INI_FILE, Encoding.GetEncoding("Shift_JIS"));

                for (int i = 0; i < lines1.Length; i++)
                {
                    line = lines1[i];
                    rows = line.Split('\t');     // 2列目以降ある場合使用

                    switch (i)
                    {
                        case 0:     // PLC_IPアドレス
                            gstrPLC_IP = rows[1];
                            break;

                        case 1:     //　ポート番号
                            gintPort = Convert.ToInt32(rows[1]);
                            txtPort.Text = gintPort.ToString();

                            break;

                        case 2:     //　ログ保存先フォルダ
                            gstrLOGpath = rows[1];
                            txtLOGpath.Text = gstrLOGpath;

                            break;

                        case 5:     // 設定画面パスワード
                            gstrPassWord = rows[1];
                            break;

                        case 9:     // ファイル保存期間(全て残す=0, 1日=1, 30日=2, 90日=3, 180日=4, 360日=5)
                            gintLOGsaveLength = Convert.ToInt32(rows[1]);
                            break;

                        case 10:    // 時間情報(None=0, 時分秒=1, 時分=2, 時のみ)
                            gintLOGtimeInfo = Convert.ToInt32(rows[1]);
                            break;

                        case 11:    // 時間付加位置(先頭=0, 末尾=1)
                            gbolLOGtimeLoc = Convert.ToBoolean(rows[1]);
                            break;

                        case 12:    // エラーログ自動削除(ON=0, OFF=1)
                            gbolLOGdelAuto = Convert.ToBoolean(rows[1]);
                            break;

                        case 15:     //　起動遅延時間（秒）
                            gintStartDelay = Convert.ToInt32(rows[1]);
                            break;

                        case 16:    // 起動遅延(ON=true, OFF=false)
                            gbolDelayOn = Convert.ToBoolean(rows[1]);
                            break;


                        default:
                            break;
                    }
                }


            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
                return false;
            }

            return true;


        }

        private void frmMain_Load(object sender, EventArgs e)
        {
            // 起動時最小化オプションで最小化表示
            if (gbolLoadFormMinimum)
            {
                this.WindowState=FormWindowState.Minimized;

            }


            // フォルダの存在確認と作成
            // ルートディレクトリ
            if (!Directory.Exists(GlbSetVal.Root_DIR))
            {
                Directory.CreateDirectory(GlbSetVal.Root_DIR);
            }

            // エラーログ
            if (!Directory.Exists(GlbSetVal.ERR_LOG_DIR))
            {
                Directory.CreateDirectory(GlbSetVal.ERR_LOG_DIR);
            }

       
            // INIファイルの確認
            if (!File.Exists(GlbSetVal.INI_FILE))
            {
                MessageBox.Show("INIファイルを確認してください。");
                return;
            }

            // INIファイルのパラメータロード
            if (!funIniLoadAndSet())
            {
                MessageBox.Show("INIファイル読込時エラーが発生しました。");
                return;
            }

            // PC_IPアドレスの表示
            subGetIPaddress();


            // 実行の遅延
            Thread.Sleep(gintStartDelay * 1000);

            // LAN接続
            if (!LAN.EthernetConnect())
            {
                MessageBox.Show("LAN接続に失敗しました。");
                return;
            }

            // ファイル名の取得
            if (!LAN.EthernetReadDataStrASC(GlbSetVal.PLC_D_FILENAME, 5, out gstrLOGfilename))
	        {
                MessageBox.Show("ファイル名取得に失敗しました。");
                return;
            }
            txtFilename.Text = gstrLOGfilename;



            // 接続中フラグセット
            gbolConnection = LAN.connectionflgPLC;


            // 集中インジケーターラベルの初期化
            subInitLabel();

            // ハートビートタイマーON
            timGetTime.Enabled = true;

            // ログ取得タイマーON
            timGetLog.Enabled = true;

        }

        private void subInitLabel() 
        {
            lblPC_Ready.BackColor = SystemColors.Control;
            lblPCsaveDone.BackColor = SystemColors.Control;
            lblPCsaveFile.BackColor = SystemColors.Control;
            lblPCturnReset.BackColor = SystemColors.Control;

            lblPLC_Ready.BackColor = SystemColors.Control;
            lblPLCcommand.BackColor = SystemColors.Control;
            lblPLCHardErr.BackColor = SystemColors.Control;
            lblPLCsaveWait.BackColor = SystemColors.Control;
            lblPLCturnReset.BackColor = SystemColors.Control;
        }

        private void subGetIPaddress()
        {  // ホスト名を取得する
            string hostname = Dns.GetHostName();

            // ホスト名からIPアドレスを取得する
            IPAddress[] adrList = Dns.GetHostAddresses(hostname);
            foreach (IPAddress address in adrList)
            {
                if (address.AddressFamily.ToString()=="InterNetwork")
                {
                    txtPC_IP.Text=address.ToString();   
                }
            }
        }

        private void frmMain_FormClosing(object sender, FormClosingEventArgs e)
        {
            if (gbolConnection)
            {
                if (
                    MessageBox.Show("LAN接続中です。切断してソフトを終了しますか？","終了の確認",
                        MessageBoxButtons.YesNo,MessageBoxIcon.Information)
                        == DialogResult.Yes)
                {
                    gbolConnection = false;

                    // ハートビートタイマーOFF
                    timGetTime.Enabled = false;

                    // ログ取得タイマーOFF
                    timGetLog.Enabled = false;

                    // LAN切断処理
                    LAN.EthernetDisConnect();
                }
            }
        }

        private void btnSetting_Click(object sender, EventArgs e)
        {
            frmPass frPass = new frmPass();
            frPass.ShowDialog();
        }

        private void timGetLog_Tick(object sender, EventArgs e)
        {
            if (funLANtrig())
            {
                // トリガータイマーの停止
                timGetLog.Enabled = false;

                // 通信ハンドシェイク start
                int num;

                // PC Ready OK
                if (LAN.EthernetWriteData(GlbSetVal.PLC_D_PC_READY,4,"0001"))
                {
                    subPaintLabelBack(lblPC_Ready);
                }
                else
                {
                    return;
                }

                    // PLC command
                   
                    do
                    {
                        if (!LAN.EthernetReadDataIntD16bit(GlbSetVal.PLC_D_PLC_COMMAND, 1, out num)) return;
                        Thread.Sleep(0);
                        Application.DoEvents();
                        if (!gbolConnection) return;

                    } while (num!=1 && num!=3);

                    subPaintLabelBack(lblPLCcommand);
                    if (num == 1)
                    {
                        // ファイル新規作成
                        if (!funCreateFileName(true))
                        {
                            return;
                        }
                    }
                    else if (num == 3)            
                    {
                        // 同じ関数だがリネーム処理を実行しない
                        if (!funCreateFileName(false))
                        {
                            return;
                        }
                    }
                  

                    // PC write start
                    if (LAN.EthernetWriteData(GlbSetVal.PLC_D_PC_SAVE,4,"0001"))
                    {
                        subPaintLabelBack(lblPCsaveFile);

                            // PLC write wait check
                            do
                            {
                                if (!LAN.EthernetReadDataIntD16bit(GlbSetVal.PLC_D_PLC_COMMAND, 1, out num))return;
                                Thread.Sleep(0);
                                Application.DoEvents();

                            } while (num != 2);

                        subPaintLabelBack(lblPLCsaveWait);

                        // ログ書き込み
                        if (!funGetLog()) { return; }

                    }
                    else
                    {
                        return;
                    }

                    // ターン終了処理
                    if (LAN.EthernetWriteData(GlbSetVal.PLC_D_PC_SAVE, 4, "0000"))
                    {
                        subPaintLabelBack(lblPCsaveDone);

                        // PLC wait check
                        do
                        {
                            if (!LAN.EthernetReadDataIntD16bit(GlbSetVal.PLC_D_PLC_READY, 0, out num)) return;
                            Thread.Sleep(0);
                            Application.DoEvents();

                        } while (num != 0);

                        subPaintLabelBack(lblPLCturnReset);

                        if (LAN.EthernetWriteData(GlbSetVal.PLC_D_PC_READY, 4, "0000"))
                        {
                            subPaintLabelBack(lblPCturnReset);
                        }
                        else
                        {
                            return;
                        }
                    }
                    else
                    {
                        return;
                    }
                    
                // ログファイルの自動削除
                if (!funAutoDelLog()) return;


                // トリガータイマーの再開
                timGetLog.Enabled = true;
            }
        }

        private bool funAutoDelLog() 
        {
           
            try
            {

                string strDate;
                DateTime dtDate;

                if (gintLOGsaveLength != 0)
                {
                    // 現在年月の取得
                    if (!LAN.EthernetReadDataStrASC(GlbSetVal.PLC_D_YMD, 3, out strDate)) return false;

                    strDate = "20" + strDate;
                    dtDate = Convert.ToDateTime( strDate.Insert(4,"/").Insert(7,"/") );

                    IEnumerable<string> strAr;
                    strAr = Directory.EnumerateDirectories(gstrLOGpath, "????", SearchOption.AllDirectories);


                    string strDatetarget;
                    DateTime dtDatetarget;
                    TimeSpan tsDelDays;
                    
                    foreach (string item in strAr)
                    {
                        // フォルダのタイムスタンプ抽出
                        strDatetarget = "20" + item.Substring(gstrLOGpath.Length).Replace("\\","");

                        if (strDatetarget.Length==8)        // サブフォルダ含めてYYYYMMDD形式のフォルダのみ抽出
                        {
                            //Console.WriteLine(strDatetarget);

                            dtDatetarget = Convert.ToDateTime(strDatetarget.Insert(4, "/").Insert(7, "/"));

                            //Console.WriteLine(dtDate.ToString() + "-" + dtDatetarget.ToString() + "=" + (dtDate - dtDatetarget));

                            switch (gintLOGsaveLength)
                            {
                                case 1:
                                    tsDelDays = TimeSpan.FromDays(2);
                                    break;
                                case 2:
                                    tsDelDays = TimeSpan.FromDays(31);
                                    break;
                                case 3:
                                    tsDelDays = TimeSpan.FromDays(91);
                                    break;
                                case 4:
                                    tsDelDays = TimeSpan.FromDays(181);
                                    break;
                                case 5:
                                    tsDelDays = TimeSpan.FromDays(361);
                                    break;
                                default:
                                    tsDelDays = TimeSpan.FromDays(1);
                                    break;
                            }

                            if ((dtDate - dtDatetarget) > tsDelDays)
                            {
                                System.IO.Directory.Delete(item,true);
                            }
                        }
                    }

                    // 親フォルダの削除
                    foreach (string item in strAr)
                    {
                        // フォルダのタイムスタンプ抽出
                        strDatetarget = "20" + item.Substring(gstrLOGpath.Length).Replace("\\", "");

                        if (strDatetarget.Length == 6)         // YYYYMMフォルダが空になっていれば消去する
                        {
                            if (
                                System.IO.Directory.GetFiles(item, "*.csv", SearchOption.AllDirectories).Length　==　0
                                )
                            {
                                System.IO.Directory.Delete(item, true);
                            }
                        }
                    
                    }

                }

                // エラーログの自動削除
                if (gbolLOGdelAuto)
                {
                    IEnumerable<string> strArErr;
                    strArErr = Directory.EnumerateFiles(GlbSetVal.ERR_LOG_DIR, "ErrLog_*.log", SearchOption.TopDirectoryOnly);
                    TimeSpan tsDelDays = TimeSpan.FromDays(GlbSetVal.ERR_DEL_DAYS);
                    foreach (string item in strArErr)
                    {
                        if (System.IO.File.GetCreationTime(item).CompareTo(DateTime.Now - tsDelDays) < 0)
	                    {
                            System.IO.File.Delete(item);
	                    }
                        
                    }
                }



            }
            catch (Exception ex)
            {
                ErrorCheck.subErrCk(ex, "funAutoDelLog","日付変換エラー");
                return false;
            }


            return true;
        }
        private bool funCheckAndRename()
        {
            try
            {
                if (File.Exists(gstrfilePath))
                {
                    // リネーム処理
                    for (int i = 0; i < GlbSetVal.RENAME_COUNT; i++)      // ※確認要
                    {
                        if (!File.Exists(gstrfilePath.Insert(gstrfilePath.Length - 4, "_" + i.ToString())))
                        {
                            gstrfilePath = gstrfilePath.Insert(gstrfilePath.Length - 4, "_" + i.ToString());
                            break;
                        }
                    }

                }
            }
            catch (Exception ex)
            {
                ErrorCheck.subErrCk(ex, "funCheckAndRename", "リネームの失敗");
                return false;
            }
           
            return true;
           

        }
        private bool funCreateTimeStamp() 
        {
          
            // ファイル名に使用するタイムスタンプの取得
            bool bol=true;
            switch (gintLOGtimeInfo)
            {

                case 0:         // 付加情報なし
                    break;
                case 1:         // 時分秒
                    bol=LAN.EthernetReadDataStrASC(GlbSetVal.PLC_D_HOUR, 3, out gstrFileTimeStamp);
                    break;

                case 2:         // 時分
                    bol=LAN.EthernetReadDataStrASC(GlbSetVal.PLC_D_HOUR, 2, out gstrFileTimeStamp);
                    break;

                case 3:         // 時のみ
                    bol=LAN.EthernetReadDataStrASC(GlbSetVal.PLC_D_HOUR, 1, out gstrFileTimeStamp);
                    break;

                default:
                    bol = false;
                    break;


            }
            return bol;
        }

        private bool funLANtrig()
        {
            int num;

            if (LAN.EthernetReadDataIntD16bit(GlbSetVal.PLC_D_PLC_READY, 1, out num))
            {
                if (num == 1)
                {
                    subPaintLabelBack(lblPLC_Ready);
                    return true;
                }
                else if (num == 64)
                {
                    subPaintLabelBack(lblPLCHardErr);
                    return false;
                }
            }

            return false;
        }

        private void subPaintLabelBack(Label lbl) 
        {
            switch (lbl.Name)
            {
                case "lblPLCHardErr":
                    lblPLCHardErr.BackColor = Color.Red;
                    break;

                case "lblPLC_Ready":
                    lblPLCHardErr.BackColor = SystemColors.Control;
                    lblPCturnReset.BackColor = SystemColors.Control;
                    lblPLC_Ready.BackColor = Color.Lime;
                    break;

                case "lblPC_Ready":
                    lblPLC_Ready.BackColor = SystemColors.Control;
                    lblPC_Ready.BackColor = Color.Lime;
                    break;

                case "lblPLCcommand":
                    lblPC_Ready.BackColor = SystemColors.Control;
                    lblPLCcommand.BackColor = Color.Lime;
                    break;

                case "lblPCsaveFile":
                    lblPLCcommand.BackColor = SystemColors.Control;
                    lblPCsaveFile.BackColor = Color.Lime;
                    break;

                case "lblPLCsaveWait":
                    lblPLCsaveWait.BackColor = Color.Lime;
                    break;

                case "lblPCsaveDone":
                    lblPCsaveFile.BackColor = SystemColors.Control;
                    lblPLCsaveWait.BackColor = SystemColors.Control;
                    lblPCsaveDone.BackColor = Color.Lime;
                    break;

                case "lblPLCturnReset":
                    lblPCsaveDone.BackColor = SystemColors.Control;
                    lblPLCturnReset.BackColor = Color.Lime;
                    break;

                case "lblPCturnReset":
                    lblPLCturnReset.BackColor = SystemColors.Control;
                    lblPCturnReset.BackColor = Color.Lime;
                    break;

                default:
                    break;
            }
        
        }

        private bool funCreateFileName(bool bol)
        {
            string YearMonth = "", Day = "";

            // ファイル名の取得
            if (!LAN.EthernetReadDataStrASC(GlbSetVal.PLC_D_FILENAME, 5, out gstrLOGfilename)) return false;
            
            txtFilename.Text = gstrLOGfilename;

            // 保存フォルダ名のタイムスタンプ取得
            if (!LAN.EthernetReadDataStrASC(GlbSetVal.PLC_D_YMD, 3, out YearMonth)) return false;
            
            
            Day = YearMonth.Substring(4, 2);
            YearMonth = YearMonth.Substring(0, 4);

            gstrfilePath = gstrLOGpath + "/" + YearMonth + "/" + Day;

            // ファイル名,保存フォルダの作成
            if (!Directory.Exists(gstrfilePath))
            {
                Directory.CreateDirectory(gstrfilePath);
            }

            // ログファイル用タイムスタンプ取得
            if (!funCreateTimeStamp()) return false;
            

            // ファイル名のタイムスタンプ位置先頭か末尾か , ファイルパスの決定
            if (gbolLOGtimeLoc)
            {
                gstrfilePath += "/" + gstrFileTimeStamp
                    + gstrLOGfilename + ".csv";

            }
            else
            {
                gstrfilePath += "/" + gstrLOGfilename
                    + gstrFileTimeStamp + ".csv";
            }


            // ファイルチェックとリネーム（新規作成時のみ実行）　　※1000回リネームでよいか？
            if (bol)
            {
                if (!funCheckAndRename()) return false;
            }
            
            return true;
        }

        private bool funGetLog()
        {
            int num = 0;
            string Timestamp = "", IDcode="";
            StringBuilder SBlog = new StringBuilder();
            int[] col;

            // Dアドレスの取得
            // タイムスタンプ, IDコード, 列数
            if (
                LAN.EthernetReadDataStrASC(GlbSetVal.PLC_D_LOG_TIME, 6, out Timestamp)
                &&
                LAN.EthernetReadDataStrASC(GlbSetVal.PLC_D_LOG_ID_CODE, 20, out IDcode)
                &&
                LAN.EthernetReadDataIntD16bit(GlbSetVal.PLC_D_LOG_COLUMN, 1, out num)
                )
            {
                // 取得データ成型
                IDcode = IDcode.TrimEnd('\0');     // 末尾のNullを除去

                SBlog.Append(Timestamp + "," + IDcode); 

                // 必要列数データ取得
               
                if (LAN.EthernetReadDataIntD16bitMulti(GlbSetVal.PLC_D_LOG_DATA, num, out col))
                {
                    foreach (int item in col)
                    {
                        SBlog.Append("," + item.ToString());
                    }
                }
                else
                {
                    return false;
                }
                
            }
            else
            {
                return false;
            }

        
            // ファイル書込み
            using (System.IO.StreamWriter Writer = new System.IO.StreamWriter(gstrfilePath, true, Encoding.Default))
            {

                Writer.WriteLine(SBlog);

            }

            return true;

        }


    }



}
