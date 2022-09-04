using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace PLCPCconnectionTool
{
    public partial class frmSettings : Form
    {
        public frmSettings()
        {
            InitializeComponent();
        }

        private void frmSettings_Load(object sender, EventArgs e)
        {
            txtPLC_IP.Text = frmMain.gstrPLC_IP;
            txtPort.Text = Convert.ToString( frmMain.gintPort);
            txtLOGpath.Text = frmMain.gstrLOGpath;
            txtFilename.Text = frmMain.gstrLOGfilename;

            // コンボボックスのセット
            subComboSet(cmbSaveLength, frmMain.gintLOGsaveLength);
            subComboSet(cmbLOGtimeInfo, frmMain.gintLOGtimeInfo);
            subComboSetBol(cmbLOGtimeLoc, frmMain.gbolLOGtimeLoc);
            subComboSetBol(cmbLOGdelAuto, frmMain.gbolLOGdelAuto);

            txtStartDeray.Text = Convert.ToString(frmMain.gintStartDelay);
            chbDelayOn.Checked = frmMain.gbolDelayOn;
        }

        private void subComboSet(ComboBox cmb, int ind) 
        {
            string str = cmb.Items[ind].ToString();
            cmb.Text = str;
        }
        private void subComboSetBol(ComboBox cmb, bool bol)
        {
            string str;
            if (bol)
            {
                str = cmb.Items[0].ToString();
            }
            else
            {
                str = cmb.Items[1].ToString();
            }
            cmb.Text = str;
        }

        private void btnCancel_Click(object sender, EventArgs e)
        {
            Close();
        }

        private void btnSave_Click(object sender, EventArgs e)
        {
            // INIファイル更新

            if ( MessageBox.Show("INIファイルを更新しますか？","更新の確認",MessageBoxButtons.YesNo)
                ==DialogResult.No)
            {
                return;
            }


            StringBuilder SB = new StringBuilder();

            string[] lines1 = System.IO.File.ReadAllLines(GlbSetVal.INI_FILE, Encoding.GetEncoding("Shift_JIS"));

            string line;
            string[] rows;

            for (int i = 0; i < lines1.Length; i++)
            {
                line = lines1[i];
                rows = line.Split('\t');     // 2列目以降ある場合使用

                switch (i)
                {
                    case 0:    // PLC_IPアドレス
                        SB.AppendLine(rows[0] + "\t" + txtPLC_IP.Text);
                        break;
                    case 1:     // ポート番号
                        SB.AppendLine(rows[0] + "\t" + txtPort.Text);
                        break;
                    case 2:     // ログ保存先フォルダ
                        SB.AppendLine(rows[0] + "\t" + txtLOGpath.Text);
                        break;

                    case 5:     // 設定画面パスワード
                        SB.AppendLine(rows[0] + "\t" + frmMain.gstrPassWord);   // パスワードは画面から変更できない
                        break;

                    case 9:     // ファイル保存期間(全て残す=0, 1日=1, 30日=2, 90日=3, 180日=4, 360日=5)
                        SB.AppendLine(rows[0] + "\t" + cmbSaveLength.SelectedIndex);
                        break;

                    case 10:     // 時間情報(None=0, 時分秒=1, 時分=2, 時のみ)
                        SB.AppendLine(rows[0] + "\t" + cmbLOGtimeInfo.SelectedIndex);
                        break;
                    case 11:     // 時間付加位置(先頭=T, 末尾=F)
                        SB.AppendLine(rows[0] + "\t" + funConvCmbVal( cmbLOGtimeLoc.SelectedIndex) );
                        break;
                    case 12:     // エラーログ自動削除(ON=T, OFF=F)
                        SB.AppendLine(rows[0] + "\t" + funConvCmbVal( cmbLOGdelAuto.SelectedIndex ));
                        break;
                    case 15:     //　起動遅延時間（秒）
                        SB.AppendLine(rows[0] + "\t" + txtStartDeray.Text);
                        break;
                    case 16:     // 起動遅延(ON=true, OFF=false)
                        SB.AppendLine(rows[0] + "\t" + chbDelayOn.Checked);
                        break;
                    default:
                        SB.AppendLine(string.Join("\t", rows));
                        break;
                }
            }



            using (System.IO.StreamWriter Writer = new System.IO.StreamWriter(
                GlbSetVal.INI_FILE, false, Encoding.Default))
            {
                Writer.Write(SB);

            }

            SB.Clear();

            MessageBox.Show("INIファイルを更新しました。\r\nソフトを再起動すると設定は有効になります。");
            Close();

        }

        private bool funConvCmbVal(int indbol)
        {
            if (indbol==0)
            {
                return true;
            }
            else
            {
                return false;
            }
        }

    }
}
