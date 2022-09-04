using System;
using System.Collections.Generic;
using System.Linq;
using System.Windows.Forms;

namespace PLCPCconnectionTool
{
    static class Program
    {
        /// <summary>
        /// アプリケーションのメイン エントリ ポイントです。
        /// </summary>
        [STAThread]
        static void Main(string[] args)
        {
            foreach (string arg in args)
            {
                if (arg=="-min")
                {
                    frmMain.gbolLoadFormMinimum = true;
                }
            }


            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            Application.Run(new frmMain());
        }
    }
}
