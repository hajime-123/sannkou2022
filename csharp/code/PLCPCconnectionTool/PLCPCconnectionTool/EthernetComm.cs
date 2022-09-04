using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Net;
using System.Net.Sockets;
using System.Threading;

namespace PLCPCconnectionTool
{
    public class EthernetComm
    {
        ////-----------------------------------------------------------
        ////　シーケンサ通信パラメータ
        ////　三菱Qシリーズのユニバーサルモデルの内蔵イーサネットでも、
        ////　外付けイーサネットでもプログラム自身は変わらない。
        ////-----------------------------------------------------------

        //サブヘッダ(5000) + ネットワークPC番号(02) + PC番号  + 要求先ユニットI/O番号(00A0)
        //QnA互換3Eフレームのコマンドを用いる限り、下記は変わらない。
        static string strSubHeadNetPcNoUnitIONo = @"500000FF03FF";

        //要求先ユニット局番号(GX-Developerで設定する局番とは関係ない)
        //QnA互換3Eフレームのコマンドを用いる限り、下記は変わらない。
        static string strUnitChNo = @"00";
        
        ////要求データ長(CPU監視タイマ～デバイス点数の文字数(16進数表記))

        ////要求(読込、書込)するデータは下記の4種類
        ////      １．着工品種情報(1～XX)  ･････　PLC→PC
        ////      ２．検査ステーションのセットブロック番号(1～XX) ･････　PLC→PC
        ////      ３．検査結果(Dレジスタ13個分) ･････　PC→PLC
        ////      ４．エラー番号･････　PC→PLC

        //データ読込データ数(16進数)：固定
        static string strDataWidthRead = @"0018";

        //データ書込データ数(16進数)：可変
        string strDataWidthWrite = "";

        //CPU監視タイマ
        static string strDataWatch = @"1000";

        //一括読み込みコマンド + サブコマンド
        static string strReadCommand = @"0401";
        static string strReadCommandS = @"0000";
        
        ////一括書込みコマンド + サブコマンド
        static string strWriteCommand = @"1401";
        static string strWriteCommandS = @"0000";

        //先頭デバイス
        static string strTopDevice = @"D*";

        //デバイスコード(10進数6桁)
        //デバイスの番号(例：D*008000　Dデバイスの8000番)
        string strCodeDevice = "";

        //デバイス点数(16進数4桁)
        //上記のデバイス番号から何点読込(書込)かの設定
        string strPointRDevice = "";
        string strPointWDevice = "";


        public bool connectionflgPLC = false;      //PLC接続フラグ


        //ソケット作成
        Socket sockPLC = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);

        //IPAddressクラスのインスタンス作成
        public IPAddress ipaPLC;


        //イーサネット接続
        public bool EthernetConnect()
        {
            try
            {
                //PLCのIPアドレス設定
                ipaPLC = IPAddress.Parse(frmMain.gstrPLC_IP);
                
                //IPアドレスとポート番号の組み合わせ設定
                System.Net.IPEndPoint ipendPLC = new System.Net.IPEndPoint(ipaPLC, frmMain.gintPort);

                //接続
                sockPLC.Connect(ipendPLC);
                
                connectionflgPLC = true;   //接続フラグ



                //正常終了
                return true;
            }
            catch(Exception ex)
            {
                //異常終了
                ErrorCheck.subErrCk(ex, "EthernetConnect", "LAN接続エラー");
                return false;
            }
        
        }

        //イーサネット切断
        public bool EthernetDisConnect()
        {
            try
            {
                //回線切断
                sockPLC.Shutdown(System.Net.Sockets.SocketShutdown.Both);
                sockPLC.Close();

                connectionflgPLC = false;   //接続フラグ

                //正常終了
                return true;

            }
            catch(Exception ex)
            {
                //異常終了
                ErrorCheck.subErrCk(ex, "EthernetDisConnect", "LAN切断エラー");
                return false;
            }

        }

//        public string funTextSend(string strCmd)
//        {
//            byte[] SData;
//            byte[] RData = new byte[256];
//            int length;

//            try
//            {
//                SData = Encoding.ASCII.GetBytes(strCmd);

//                //データ送信
////                length = sockIDGB.Send(SData, SData.Length, System.Net.Sockets.SocketFlags.None);


////                length = sockIDGB.Receive(RData, RData.Length, System.Net.Sockets.SocketFlags.None);

//                //バイト列からASCII文字列に
////                string chars = (Encoding.ASCII.GetString(RData, 0, RData.Length)).Substring(0, length);
//                //Console.WriteLine(chars);     //確認用


////                return chars;
//            }
//            catch (Exception ex)
//            {

//                ErrorCheck.subErrCk(ex, "funTextSend", "LAN送受信エラー");
//                return "";
//            }

//        }

        //イーサネットデータ数値読込 1D=16bit 1ワードのみ
        public bool EthernetReadDataIntD16bit(string stdevno, int num, out int d1)
        //public bool EthernetReadDataIntD16bit(string stdevno, int num, out int d1, out bool errflg_temp, out string errstr_temp)
        {
            //stdevno   :スタートデバイス番号
            //num       ：データ(ワード)数
            //d1        ：読込データ



            byte[] SData;
            byte[] RData = new byte[256];
            int length;

            try
            {
                strCodeDevice = String.Format("{0:000000}", int.Parse(stdevno));  //指定文字列について6文字になるまで先頭を"0"で埋める
                strPointRDevice = num.ToString("X4");           //データ(ワード)数を16進数に変換後4桁表示

                SData = Encoding.ASCII.GetBytes(strSubHeadNetPcNoUnitIONo + strUnitChNo + strDataWidthRead + strDataWatch + strReadCommand
                                  + strReadCommandS + strTopDevice + strCodeDevice + strPointRDevice);

                //データ送信
                length = sockPLC.Send(SData, SData.Length, System.Net.Sockets.SocketFlags.None);

                //シーケンサCPUからの応答伝文(レスポンス)待ち
                //Thread.Sleep(100);
                length = sockPLC.Receive(RData, RData.Length, System.Net.Sockets.SocketFlags.None);

                //バイト列からASCII文字列に
                string chars = (Encoding.ASCII.GetString(RData, 0, RData.Length)).Substring(0, length);
                //Console.WriteLine(chars);     //確認用

                //Thread.Sleep(10);

                //(16進数文字列4桁を10進数にする)
                d1 = (int)Convert.ToInt16(chars.Substring(chars.Length - 4 , 4 ), 16);

                //正常終了
                //errflg_temp = false;
                //errflg_temp = true;
                //errstr_temp = "OK";
                return true;

            }
            catch (Exception ex)
            {
                //異常終了
                //errflg_temp = false;
                //errstr_temp = "イーサネットデータ読込エラー";
                d1 = 9999;  //異常値代入
                ErrorCheck.subErrCk(ex, "EthernetReadDataIntD16bit", "Dアドレス数値読み込みエラー");
                return false;

            }

        }

        //イーサネットデータ数値読込 1D=16bit 複数ワード
        public bool EthernetReadDataIntD16bitMulti(string stdevno, int num, out int[] dm)
        {
            //stdevno   :スタートデバイス番号
            //num       ：データ(ワード)数
            //d1        ：読込データ



            byte[] SData;
            byte[] RData = new byte[4096];
            int length;
            dm = new int[num];

            try
            {
                strCodeDevice = String.Format("{0:000000}", int.Parse(stdevno));  //指定文字列について6文字になるまで先頭を"0"で埋める
                strPointRDevice = num.ToString("X4");           //データ(ワード)数を16進数に変換後4桁表示

                SData = Encoding.ASCII.GetBytes(strSubHeadNetPcNoUnitIONo + strUnitChNo + strDataWidthRead + strDataWatch + strReadCommand
                                  + strReadCommandS + strTopDevice + strCodeDevice + strPointRDevice);

                //データ送信
                length = sockPLC.Send(SData, SData.Length, System.Net.Sockets.SocketFlags.None);

                //シーケンサCPUからの応答伝文(レスポンス)待ち
                //Thread.Sleep(100);
                length = sockPLC.Receive(RData, RData.Length, System.Net.Sockets.SocketFlags.None);

                //バイト列からASCII文字列に
                string chars = (Encoding.ASCII.GetString(RData, 0, RData.Length)).Substring(0, length);
                //Console.WriteLine(chars);     //確認用

                //Thread.Sleep(10);

                //(16進数文字列4桁を10進数にする)
                int dTemp = 0;

                for (int i = num; i > 0; i--)
                {
                    dTemp = (int)Convert.ToInt16(chars.Substring(chars.Length - 4 * i, 4), 16);
                    dm[num - i] = dTemp;
                }

                //正常終了
                //errflg_temp = false;
                //errflg_temp = true;
                //errstr_temp = "OK";
                return true;

            }
            catch (Exception ex)
            {
                //異常終了
                //errflg_temp = false;
                //errstr_temp = "イーサネットデータ読込エラー";
                dm[0] = 99999;  //異常値代入
                ErrorCheck.subErrCk(ex, "EthernetReadDataIntD16bitMulti", "Dアドレス数値複数読み込みエラー");
                return false;

            }

        }

        ////イーサネットデータ数値読込 1D=32bit
        //public void EthernetReadDataIntD32bit(string stdevno, int num, out int d1, out bool errflg_temp, out string errstr_temp)
        //{
        //    //stdevno   :スタートデバイス番号
        //    //num       ：データ(ワード)数
        //    //d1        ：読込データ




        //    byte[] SData;
        //    byte[] RData = new byte[256];
        //    int length;
        //    string D1, D2;
        //    try
        //    {
        //        strCodeDevice = String.Format("{0:000000}", int.Parse(stdevno));  //指定文字列について6文字になるまで先頭を"0"で埋める
        //        strPointRDevice = num.ToString("X4");           //データ(ワード)数を16進数に変換後4桁表示

        //        SData = Encoding.ASCII.GetBytes(strSubHeadNetPcNoUnitIONo + strUnitChNo + strDataWidthRead + strDataWatch + strReadCommand
        //                          + strReadCommandS + strTopDevice + strCodeDevice + strPointRDevice);

        //        //データ送信
        //        length = sock.Send(SData, SData.Length, System.Net.Sockets.SocketFlags.None);

        //        //シーケンサCPUからの応答伝文(レスポンス)待ち
        //        Thread.Sleep(100);
        //        length = sock.Receive(RData, RData.Length, System.Net.Sockets.SocketFlags.None);

        //        //バイト列からASCII文字列に
        //        string chars = (Encoding.ASCII.GetString(RData, 0, RData.Length)).Substring(0, length);
        //        //Console.WriteLine(chars);     //確認用

        //        Thread.Sleep(10);

        //        // 32bit用の文字列整形
        //        D1 = chars.Substring(chars.Length - 8, 4);
        //        D2 = chars.Substring(chars.Length - 4, 4);

        //        //(16進数文字列 8 桁を10進数にする)
        //        d1 = Convert.ToInt32( D2+D1 , 16);

        //        //正常終了
        //        errflg_temp = false;
        //        errstr_temp = "OK";
        //        //return 0;

        //    }
        //    catch
        //    {
        //        //異常終了
        //        errflg_temp = true;
        //        errstr_temp = "イーサネットデータ読込エラー";
        //        d1 = 99999;  //異常値代入
        //        //return 11020;
        //    }

        //}

        //イーサネットデータ文字列読込
//        public void EthernetReadDataStrASC(string stdevno, int num, out string strResult, out bool errflg_temp, out string errstr_temp)
        public bool EthernetReadDataStrASC(string stdevno, int num, out string strResult)
        {
            //stdevno   :スタートデバイス番号
            //num       ：データ(ワード)数
            //d1        ：読込データ

            byte[] SData;
            byte[] RData = new byte[256];
            int length;
            StringBuilder SBresult = new StringBuilder();
            char chrN1;
            string strN;


            try
            {
                strCodeDevice = String.Format("{0:000000}", int.Parse(stdevno));  //指定文字列について6文字になるまで先頭を"0"で埋める
                strPointRDevice = num.ToString("X4");           //データ(ワード)数を16進数に変換後4桁表示

                SData = Encoding.ASCII.GetBytes(strSubHeadNetPcNoUnitIONo + strUnitChNo + strDataWidthRead + strDataWatch + strReadCommand
                                  + strReadCommandS + strTopDevice + strCodeDevice + strPointRDevice);

                //データ送信
                length = sockPLC.Send(SData, SData.Length, System.Net.Sockets.SocketFlags.None);

                //シーケンサCPUからの応答伝文(レスポンス)待ち
//                Thread.Sleep(100);
                length = sockPLC.Receive(RData, RData.Length, System.Net.Sockets.SocketFlags.None);

                //バイト列からASCII文字列に
                string chars = (Encoding.ASCII.GetString(RData, 0, RData.Length)).Substring(0, length);
                //Console.WriteLine(chars);     //確認用

              //  Thread.Sleep(10);

                // 文字列整形
                chars = chars.Substring(chars.Length - (num * 4), num * 4);     // 必要な部分を抽出

                for (int i = 0; i < chars.Length; i++)
                {
                    strN = chars.Substring(i, 4);               // ４文字取得

                    for (int t = 2; t >= 0; t--)        // for文をStepに変更したい！みにくい
                    {
                        chrN1 = Convert.ToChar(Convert.ToInt32(strN.Substring(t, 2), 16));        // char変換 して入替え
                        t--;

                        SBresult.Append(chrN1.ToString());                                       // 文字列に直す
                    }

                    i = i + 3;
                }

                strResult = SBresult.ToString();

                strResult = strResult.Trim();

                SBresult.Clear();

                //正常終了
                //errflg_temp = false;
                //errstr_temp = "OK";
                return true;

            }
            catch (Exception ex)
            {
                //異常終了
                //errflg_temp = true;
                //errstr_temp = "イーサネットデータ読込エラー";
                strResult = "XXXXX";  //異常値代入
               // return 11020;
                ErrorCheck.subErrCk(ex, "EthernetReadDataStrASC", "Dアドレス文字列読み込みエラー");
                return false;
            }

        }

        //// マーキング部　結果の読み込み
        //public int EthernetReadDataStrJUD(string stdevno, int num, out string strResult, out bool errflg_temp, out string errstr_temp)
        //{
        //    //stdevno   :スタートデバイス番号
        //    //num       ：データ(ワード)数
        //    //d1        ：読込データ

        //    byte[] SData;
        //    byte[] RData = new byte[132 + num * 4];         // ヘッダ132文字固定
        //    int length;
        //    StringBuilder SBresult = new StringBuilder();
        //    string strN;
        //    string strbit, binbit;
        //    int hexbit;

        //    try
        //    {
        //        strCodeDevice = String.Format("{0:000000}", int.Parse(stdevno));  //指定文字列について6文字になるまで先頭を"0"で埋める
        //        strPointRDevice = num.ToString("X4");           //データ(ワード)数を16進数に変換後4桁表示

        //        SData = Encoding.ASCII.GetBytes(strSubHeadNetPcNoUnitIONo + strUnitChNo + strDataWidthRead + strDataWatch + strReadCommand
        //                          + strReadCommandS + strTopDevice + strCodeDevice + strPointRDevice);

        //        //データ送信
        //        length = sock.Send(SData, SData.Length, System.Net.Sockets.SocketFlags.None);

        //        //シーケンサCPUからの応答伝文(レスポンス)待ち
        //        Thread.Sleep(100);
        //        length = sock.Receive(RData, RData.Length, System.Net.Sockets.SocketFlags.None);

        //        //バイト列からASCII文字列に
        //        string chars = (Encoding.ASCII.GetString(RData, 0, RData.Length)).Substring(0, length);
        //        //Console.WriteLine(chars);     //確認用

        //        Thread.Sleep(10);

        //        // 文字列整形
        //        chars = chars.Substring(chars.Length - (num * 4), num * 4);     // 必要な部分を抽出　※端数分含む



        //        for (int i = 0; i < chars.Length; i++)      // for文をStepに変更したい！みにくい
        //        {
        //            strN = chars.Substring(i, 4);               // ４文字（１ワード分）取得

        //            hexbit = Convert.ToInt32(strN, 16);                       // 16進数を数値化
        //            binbit = Convert.ToString(hexbit, 2).PadLeft(16, '0');        // 16進数→2進数文字列に変換、16桁化(左0埋め)

        //            for (int t = 15; t >= 0; t--)            // ワード内のbitを並べ替え
        //            {
        //                strbit = binbit.Substring(t, 1);        // １文字取得
        //                SBresult.Append(strbit);                                       // 追記
        //            }

        //            i = i + 3;
        //        }

        //        strResult = SBresult.ToString();        // まだ端数部分含んでる



        //        SBresult.Clear();

        //        //正常終了
        //        errflg_temp = false;
        //        errstr_temp = "OK";
        //        return 0;

        //    }
        //    catch
        //    {
        //        //異常終了
        //        errflg_temp = true;
        //        errstr_temp = "イーサネットデータ読込エラー";
        //        strResult = "XXXXX";  //異常値代入
        //        return 11020;
        //    }

        //}

        //イーサネットデータ書込
        public bool EthernetWriteData(string stdevno, int num, string WRData)
        {
            //stdevno   ：スタートデバイス番号
            //num       ：データ数(ワード数の16進表記、例：52文字-13ワード×4文字(16進数))
            //WRData    ：書込みデータ

            try
            {
                byte[] SData;
                byte[] RData = new byte[512];
                int Retcode;

                //指定文字列について6文字になるまで先頭を"0"で埋める
                //strCodeDevice = String.Format("{0:000000}", int.Parse(stdevno));
                strCodeDevice = stdevno.PadLeft(6, '0');
                strDataWidthWrite = (num + 24).ToString("X4");           //書込データ文字数
                strPointWDevice = (num / 4).ToString("X4");               //書込データ数(ワード数：16進数)

                //指定したデバイス番号からワード数分(例：データ数:52文字の場合13ワード(16進数文字列))一括書き込み
                SData = Encoding.ASCII.GetBytes(strSubHeadNetPcNoUnitIONo + strUnitChNo + strDataWidthWrite + strDataWatch + strWriteCommand
                                  + strWriteCommandS + strTopDevice + strCodeDevice + strPointWDevice + WRData);

                //Console.WriteLine(strSubHeadNetPcNoUnitIONo + strUnitChNo + strDataWidthWrite + strDataWatch + strWriteCommand
                //                  + strWriteCommandS + strTopDevice + strCodeDevice + strPointWDevice + WRData);

                //データを送信
                Retcode = sockPLC.Send(SData, SData.Length, System.Net.Sockets.SocketFlags.None);

                Retcode = sockPLC.Receive(RData, RData.Length, System.Net.Sockets.SocketFlags.None);


                //シーケンサCPUからの応答伝文(レスポンス)を読み出します。
                //Thread.Sleep(300);

                //正常終了
                //errflg_temp = false;
                //errstr_temp = "OK";
                return true;

            }
            catch(Exception ex)
            {
                //異常終了
                //errflg_temp = true;
                //errstr_temp = "イーサネットデータ書込エラー";
                ErrorCheck.subErrCk(ex, "EthernetWriteData", "EthernetComm");
                return false;
            }

        }

    }
}
