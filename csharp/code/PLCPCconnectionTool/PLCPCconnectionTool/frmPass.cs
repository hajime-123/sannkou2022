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
    public partial class frmPass : Form
    {
        public frmPass()
        {
            InitializeComponent();
        }

        private void txtPass_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == System.Windows.Forms.Keys.Enter)
            {

                if (txtPass.Text == frmMain.gstrPassWord)
                {
                    frmSettings frSetings = new frmSettings();
                    frSetings.ShowDialog();
                }

                Close();
            }
        }

        private void btnCancel_Click(object sender, EventArgs e)
        {
            Close();
        }
    }
}
