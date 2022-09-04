namespace PLCPCconnectionTool
{
    partial class frmMain
    {
        /// <summary>
        /// 必要なデザイナー変数です。
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 使用中のリソースをすべてクリーンアップします。
        /// </summary>
        /// <param name="disposing">マネージ リソースが破棄される場合 true、破棄されない場合は false です。</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows フォーム デザイナーで生成されたコード

        /// <summary>
        /// デザイナー サポートに必要なメソッドです。このメソッドの内容を
        /// コード エディターで変更しないでください。
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            this.timGetTime = new System.Windows.Forms.Timer(this.components);
            this.lblTimeNow = new System.Windows.Forms.Label();
            this.btnSetting = new System.Windows.Forms.Button();
            this.lblPC_IP = new System.Windows.Forms.Label();
            this.lblPort = new System.Windows.Forms.Label();
            this.lblLOGpath = new System.Windows.Forms.Label();
            this.txtPC_IP = new System.Windows.Forms.TextBox();
            this.txtPort = new System.Windows.Forms.TextBox();
            this.txtLOGpath = new System.Windows.Forms.TextBox();
            this.timGetLog = new System.Windows.Forms.Timer(this.components);
            this.txtFilename = new System.Windows.Forms.TextBox();
            this.lblFilename = new System.Windows.Forms.Label();
            this.lblPLC_Ready = new System.Windows.Forms.Label();
            this.lblPLCHardErr = new System.Windows.Forms.Label();
            this.lblPC_Ready = new System.Windows.Forms.Label();
            this.lblPLCcommand = new System.Windows.Forms.Label();
            this.lblPCsaveFile = new System.Windows.Forms.Label();
            this.lblPLCsaveWait = new System.Windows.Forms.Label();
            this.lblPCsaveDone = new System.Windows.Forms.Label();
            this.lblPLCturnReset = new System.Windows.Forms.Label();
            this.lblPCturnReset = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // timGetTime
            // 
            this.timGetTime.Interval = 1000;
            this.timGetTime.Tick += new System.EventHandler(this.timGetTime_Tick);
            // 
            // lblTimeNow
            // 
            this.lblTimeNow.AutoSize = true;
            this.lblTimeNow.Location = new System.Drawing.Point(399, 19);
            this.lblTimeNow.Name = "lblTimeNow";
            this.lblTimeNow.Size = new System.Drawing.Size(117, 12);
            this.lblTimeNow.TabIndex = 0;
            this.lblTimeNow.Text = "yyyy/mm/dd tt:mm:ss";
            // 
            // btnSetting
            // 
            this.btnSetting.Location = new System.Drawing.Point(379, 249);
            this.btnSetting.Name = "btnSetting";
            this.btnSetting.Size = new System.Drawing.Size(75, 23);
            this.btnSetting.TabIndex = 1;
            this.btnSetting.Text = "設定変更";
            this.btnSetting.UseVisualStyleBackColor = true;
            this.btnSetting.Click += new System.EventHandler(this.btnSetting_Click);
            // 
            // lblPC_IP
            // 
            this.lblPC_IP.AutoSize = true;
            this.lblPC_IP.Location = new System.Drawing.Point(69, 196);
            this.lblPC_IP.Name = "lblPC_IP";
            this.lblPC_IP.Size = new System.Drawing.Size(74, 12);
            this.lblPC_IP.TabIndex = 2;
            this.lblPC_IP.Text = "PC　IPアドレス";
            // 
            // lblPort
            // 
            this.lblPort.AutoSize = true;
            this.lblPort.Location = new System.Drawing.Point(62, 218);
            this.lblPort.Name = "lblPort";
            this.lblPort.Size = new System.Drawing.Size(81, 12);
            this.lblPort.TabIndex = 3;
            this.lblPort.Text = "使用ポート番号";
            // 
            // lblLOGpath
            // 
            this.lblLOGpath.AutoSize = true;
            this.lblLOGpath.Location = new System.Drawing.Point(67, 240);
            this.lblLOGpath.Name = "lblLOGpath";
            this.lblLOGpath.Size = new System.Drawing.Size(76, 12);
            this.lblLOGpath.TabIndex = 4;
            this.lblLOGpath.Text = "保存先フォルダ";
            // 
            // txtPC_IP
            // 
            this.txtPC_IP.Location = new System.Drawing.Point(149, 193);
            this.txtPC_IP.Name = "txtPC_IP";
            this.txtPC_IP.ReadOnly = true;
            this.txtPC_IP.Size = new System.Drawing.Size(86, 19);
            this.txtPC_IP.TabIndex = 5;
            this.txtPC_IP.TabStop = false;
            // 
            // txtPort
            // 
            this.txtPort.Location = new System.Drawing.Point(149, 215);
            this.txtPort.Name = "txtPort";
            this.txtPort.ReadOnly = true;
            this.txtPort.Size = new System.Drawing.Size(57, 19);
            this.txtPort.TabIndex = 5;
            this.txtPort.TabStop = false;
            // 
            // txtLOGpath
            // 
            this.txtLOGpath.Location = new System.Drawing.Point(149, 237);
            this.txtLOGpath.Name = "txtLOGpath";
            this.txtLOGpath.ReadOnly = true;
            this.txtLOGpath.Size = new System.Drawing.Size(205, 19);
            this.txtLOGpath.TabIndex = 5;
            this.txtLOGpath.TabStop = false;
            // 
            // timGetLog
            // 
            this.timGetLog.Interval = 200;
            this.timGetLog.Tick += new System.EventHandler(this.timGetLog_Tick);
            // 
            // txtFilename
            // 
            this.txtFilename.Location = new System.Drawing.Point(149, 262);
            this.txtFilename.Name = "txtFilename";
            this.txtFilename.ReadOnly = true;
            this.txtFilename.Size = new System.Drawing.Size(205, 19);
            this.txtFilename.TabIndex = 5;
            this.txtFilename.TabStop = false;
            // 
            // lblFilename
            // 
            this.lblFilename.AutoSize = true;
            this.lblFilename.Location = new System.Drawing.Point(92, 265);
            this.lblFilename.Name = "lblFilename";
            this.lblFilename.Size = new System.Drawing.Size(51, 12);
            this.lblFilename.TabIndex = 4;
            this.lblFilename.Text = "ファイル名";
            // 
            // lblPLC_Ready
            // 
            this.lblPLC_Ready.AutoSize = true;
            this.lblPLC_Ready.BackColor = System.Drawing.Color.Lime;
            this.lblPLC_Ready.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.lblPLC_Ready.Location = new System.Drawing.Point(127, 19);
            this.lblPLC_Ready.Name = "lblPLC_Ready";
            this.lblPLC_Ready.Size = new System.Drawing.Size(64, 14);
            this.lblPLC_Ready.TabIndex = 0;
            this.lblPLC_Ready.Text = "PLC Ready";
            // 
            // lblPLCHardErr
            // 
            this.lblPLCHardErr.AutoSize = true;
            this.lblPLCHardErr.BackColor = System.Drawing.Color.Red;
            this.lblPLCHardErr.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.lblPLCHardErr.Location = new System.Drawing.Point(210, 19);
            this.lblPLCHardErr.Name = "lblPLCHardErr";
            this.lblPLCHardErr.Size = new System.Drawing.Size(55, 14);
            this.lblPLCHardErr.TabIndex = 0;
            this.lblPLCHardErr.Text = "装置異常";
            // 
            // lblPC_Ready
            // 
            this.lblPC_Ready.AutoSize = true;
            this.lblPC_Ready.BackColor = System.Drawing.Color.Lime;
            this.lblPC_Ready.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.lblPC_Ready.Location = new System.Drawing.Point(45, 40);
            this.lblPC_Ready.Name = "lblPC_Ready";
            this.lblPC_Ready.Size = new System.Drawing.Size(58, 14);
            this.lblPC_Ready.TabIndex = 0;
            this.lblPC_Ready.Text = "PC Ready";
            // 
            // lblPLCcommand
            // 
            this.lblPLCcommand.AutoSize = true;
            this.lblPLCcommand.BackColor = System.Drawing.Color.Lime;
            this.lblPLCcommand.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.lblPLCcommand.Location = new System.Drawing.Point(127, 61);
            this.lblPLCcommand.Name = "lblPLCcommand";
            this.lblPLCcommand.Size = new System.Drawing.Size(71, 14);
            this.lblPLCcommand.TabIndex = 0;
            this.lblPLCcommand.Text = "PLC comand";
            // 
            // lblPCsaveFile
            // 
            this.lblPCsaveFile.AutoSize = true;
            this.lblPCsaveFile.BackColor = System.Drawing.Color.Lime;
            this.lblPCsaveFile.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.lblPCsaveFile.Location = new System.Drawing.Point(45, 75);
            this.lblPCsaveFile.Name = "lblPCsaveFile";
            this.lblPCsaveFile.Size = new System.Drawing.Size(62, 14);
            this.lblPCsaveFile.TabIndex = 0;
            this.lblPCsaveFile.Text = "PC 保存中";
            // 
            // lblPLCsaveWait
            // 
            this.lblPLCsaveWait.AutoSize = true;
            this.lblPLCsaveWait.BackColor = System.Drawing.Color.Lime;
            this.lblPLCsaveWait.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.lblPLCsaveWait.Location = new System.Drawing.Point(127, 98);
            this.lblPLCsaveWait.Name = "lblPLCsaveWait";
            this.lblPLCsaveWait.Size = new System.Drawing.Size(77, 14);
            this.lblPLCsaveWait.TabIndex = 0;
            this.lblPLCsaveWait.Text = "PLC 保存待ち";
            // 
            // lblPCsaveDone
            // 
            this.lblPCsaveDone.AutoSize = true;
            this.lblPCsaveDone.BackColor = System.Drawing.Color.Lime;
            this.lblPCsaveDone.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.lblPCsaveDone.Location = new System.Drawing.Point(45, 118);
            this.lblPCsaveDone.Name = "lblPCsaveDone";
            this.lblPCsaveDone.Size = new System.Drawing.Size(74, 14);
            this.lblPCsaveDone.TabIndex = 0;
            this.lblPCsaveDone.Text = "PC 保存完了";
            // 
            // lblPLCturnReset
            // 
            this.lblPLCturnReset.AutoSize = true;
            this.lblPLCturnReset.BackColor = System.Drawing.Color.Lime;
            this.lblPLCturnReset.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.lblPLCturnReset.Location = new System.Drawing.Point(127, 134);
            this.lblPLCturnReset.Name = "lblPLCturnReset";
            this.lblPLCturnReset.Size = new System.Drawing.Size(91, 14);
            this.lblPLCturnReset.TabIndex = 0;
            this.lblPLCturnReset.Text = "PLC ターンリセット";
            // 
            // lblPCturnReset
            // 
            this.lblPCturnReset.AutoSize = true;
            this.lblPCturnReset.BackColor = System.Drawing.Color.Lime;
            this.lblPCturnReset.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.lblPCturnReset.Location = new System.Drawing.Point(45, 158);
            this.lblPCturnReset.Name = "lblPCturnReset";
            this.lblPCturnReset.Size = new System.Drawing.Size(85, 14);
            this.lblPCturnReset.TabIndex = 0;
            this.lblPCturnReset.Text = "PC ターンリセット";
            // 
            // frmMain
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(519, 296);
            this.Controls.Add(this.lblPLCHardErr);
            this.Controls.Add(this.lblPLCturnReset);
            this.Controls.Add(this.lblPLCsaveWait);
            this.Controls.Add(this.lblPLCcommand);
            this.Controls.Add(this.lblPCturnReset);
            this.Controls.Add(this.lblPCsaveDone);
            this.Controls.Add(this.lblPCsaveFile);
            this.Controls.Add(this.lblPC_Ready);
            this.Controls.Add(this.lblPLC_Ready);
            this.Controls.Add(this.txtFilename);
            this.Controls.Add(this.txtLOGpath);
            this.Controls.Add(this.txtPort);
            this.Controls.Add(this.txtPC_IP);
            this.Controls.Add(this.lblFilename);
            this.Controls.Add(this.lblLOGpath);
            this.Controls.Add(this.lblPort);
            this.Controls.Add(this.lblPC_IP);
            this.Controls.Add(this.btnSetting);
            this.Controls.Add(this.lblTimeNow);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.Fixed3D;
            this.MaximizeBox = false;
            this.Name = "frmMain";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "PLC⇔PC汎用通信システム";
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.frmMain_FormClosing);
            this.Load += new System.EventHandler(this.frmMain_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Timer timGetTime;
        private System.Windows.Forms.Label lblTimeNow;
        private System.Windows.Forms.Button btnSetting;
        private System.Windows.Forms.Label lblPC_IP;
        private System.Windows.Forms.Label lblPort;
        private System.Windows.Forms.Label lblLOGpath;
        private System.Windows.Forms.TextBox txtPC_IP;
        private System.Windows.Forms.TextBox txtPort;
        private System.Windows.Forms.TextBox txtLOGpath;
        private System.Windows.Forms.Timer timGetLog;
        private System.Windows.Forms.TextBox txtFilename;
        private System.Windows.Forms.Label lblFilename;
        private System.Windows.Forms.Label lblPLC_Ready;
        private System.Windows.Forms.Label lblPLCHardErr;
        private System.Windows.Forms.Label lblPC_Ready;
        private System.Windows.Forms.Label lblPLCcommand;
        private System.Windows.Forms.Label lblPCsaveFile;
        private System.Windows.Forms.Label lblPLCsaveWait;
        private System.Windows.Forms.Label lblPCsaveDone;
        private System.Windows.Forms.Label lblPLCturnReset;
        private System.Windows.Forms.Label lblPCturnReset;
    }
}

