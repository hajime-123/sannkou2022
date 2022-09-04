namespace PLCPCconnectionTool
{
    partial class frmSettings
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.btnSave = new System.Windows.Forms.Button();
            this.btnCancel = new System.Windows.Forms.Button();
            this.txtPLC_IP = new System.Windows.Forms.TextBox();
            this.txtPort = new System.Windows.Forms.TextBox();
            this.txtLOGpath = new System.Windows.Forms.TextBox();
            this.cmbLOGtimeInfo = new System.Windows.Forms.ComboBox();
            this.cmbLOGtimeLoc = new System.Windows.Forms.ComboBox();
            this.cmbLOGdelAuto = new System.Windows.Forms.ComboBox();
            this.txtStartDeray = new System.Windows.Forms.TextBox();
            this.chbDelayOn = new System.Windows.Forms.CheckBox();
            this.txtFilename = new System.Windows.Forms.TextBox();
            this.lblPLC_IP = new System.Windows.Forms.Label();
            this.lblPort = new System.Windows.Forms.Label();
            this.lblLOGsavePath = new System.Windows.Forms.Label();
            this.lblFilename = new System.Windows.Forms.Label();
            this.lblLOGtimestamp = new System.Windows.Forms.Label();
            this.lblLOGtimeLoc = new System.Windows.Forms.Label();
            this.lblLOGdelAuto = new System.Windows.Forms.Label();
            this.lblStartDelay = new System.Windows.Forms.Label();
            this.cmbSaveLength = new System.Windows.Forms.ComboBox();
            this.lblSaveLength = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // btnSave
            // 
            this.btnSave.Location = new System.Drawing.Point(260, 236);
            this.btnSave.Name = "btnSave";
            this.btnSave.Size = new System.Drawing.Size(75, 23);
            this.btnSave.TabIndex = 0;
            this.btnSave.Text = "保存";
            this.btnSave.UseVisualStyleBackColor = true;
            this.btnSave.Click += new System.EventHandler(this.btnSave_Click);
            // 
            // btnCancel
            // 
            this.btnCancel.Location = new System.Drawing.Point(260, 276);
            this.btnCancel.Name = "btnCancel";
            this.btnCancel.Size = new System.Drawing.Size(75, 23);
            this.btnCancel.TabIndex = 0;
            this.btnCancel.Text = "キャンセル";
            this.btnCancel.UseVisualStyleBackColor = true;
            this.btnCancel.Click += new System.EventHandler(this.btnCancel_Click);
            // 
            // txtPLC_IP
            // 
            this.txtPLC_IP.Location = new System.Drawing.Point(96, 35);
            this.txtPLC_IP.Name = "txtPLC_IP";
            this.txtPLC_IP.Size = new System.Drawing.Size(85, 19);
            this.txtPLC_IP.TabIndex = 1;
            this.txtPLC_IP.Text = "192.168.xxx.xxx";
            this.txtPLC_IP.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // txtPort
            // 
            this.txtPort.Location = new System.Drawing.Point(96, 60);
            this.txtPort.Name = "txtPort";
            this.txtPort.Size = new System.Drawing.Size(43, 19);
            this.txtPort.TabIndex = 1;
            this.txtPort.Text = "99999";
            this.txtPort.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // txtLOGpath
            // 
            this.txtLOGpath.Location = new System.Drawing.Point(96, 98);
            this.txtLOGpath.Name = "txtLOGpath";
            this.txtLOGpath.Size = new System.Drawing.Size(220, 19);
            this.txtLOGpath.TabIndex = 1;
            this.txtLOGpath.Text = "C:\\";
            // 
            // cmbLOGtimeInfo
            // 
            this.cmbLOGtimeInfo.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.cmbLOGtimeInfo.FormattingEnabled = true;
            this.cmbLOGtimeInfo.Items.AddRange(new object[] {
            "付加なし",
            "時・分・秒",
            "時・分",
            "時"});
            this.cmbLOGtimeInfo.Location = new System.Drawing.Point(96, 175);
            this.cmbLOGtimeInfo.Name = "cmbLOGtimeInfo";
            this.cmbLOGtimeInfo.Size = new System.Drawing.Size(121, 20);
            this.cmbLOGtimeInfo.TabIndex = 2;
            // 
            // cmbLOGtimeLoc
            // 
            this.cmbLOGtimeLoc.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.cmbLOGtimeLoc.FormattingEnabled = true;
            this.cmbLOGtimeLoc.Items.AddRange(new object[] {
            "先頭",
            "末尾"});
            this.cmbLOGtimeLoc.Location = new System.Drawing.Point(96, 201);
            this.cmbLOGtimeLoc.Name = "cmbLOGtimeLoc";
            this.cmbLOGtimeLoc.Size = new System.Drawing.Size(70, 20);
            this.cmbLOGtimeLoc.TabIndex = 2;
            // 
            // cmbLOGdelAuto
            // 
            this.cmbLOGdelAuto.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.cmbLOGdelAuto.FormattingEnabled = true;
            this.cmbLOGdelAuto.Items.AddRange(new object[] {
            "ON",
            "OFF"});
            this.cmbLOGdelAuto.Location = new System.Drawing.Point(96, 227);
            this.cmbLOGdelAuto.Name = "cmbLOGdelAuto";
            this.cmbLOGdelAuto.Size = new System.Drawing.Size(70, 20);
            this.cmbLOGdelAuto.TabIndex = 2;
            // 
            // txtStartDeray
            // 
            this.txtStartDeray.Location = new System.Drawing.Point(107, 258);
            this.txtStartDeray.Name = "txtStartDeray";
            this.txtStartDeray.Size = new System.Drawing.Size(32, 19);
            this.txtStartDeray.TabIndex = 1;
            this.txtStartDeray.Text = "999";
            this.txtStartDeray.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // chbDelayOn
            // 
            this.chbDelayOn.AutoSize = true;
            this.chbDelayOn.Location = new System.Drawing.Point(148, 260);
            this.chbDelayOn.Name = "chbDelayOn";
            this.chbDelayOn.Size = new System.Drawing.Size(72, 16);
            this.chbDelayOn.TabIndex = 3;
            this.chbDelayOn.Text = "遅延実行";
            this.chbDelayOn.UseVisualStyleBackColor = true;
            // 
            // txtFilename
            // 
            this.txtFilename.Enabled = false;
            this.txtFilename.Location = new System.Drawing.Point(96, 123);
            this.txtFilename.Name = "txtFilename";
            this.txtFilename.ReadOnly = true;
            this.txtFilename.Size = new System.Drawing.Size(77, 19);
            this.txtFilename.TabIndex = 1;
            this.txtFilename.Text = "01234567890";
            // 
            // lblPLC_IP
            // 
            this.lblPLC_IP.AutoSize = true;
            this.lblPLC_IP.Location = new System.Drawing.Point(12, 38);
            this.lblPLC_IP.Name = "lblPLC_IP";
            this.lblPLC_IP.Size = new System.Drawing.Size(82, 12);
            this.lblPLC_IP.TabIndex = 4;
            this.lblPLC_IP.Text = "PLC IPアドレス：";
            // 
            // lblPort
            // 
            this.lblPort.AutoSize = true;
            this.lblPort.Location = new System.Drawing.Point(7, 63);
            this.lblPort.Name = "lblPort";
            this.lblPort.Size = new System.Drawing.Size(87, 12);
            this.lblPort.TabIndex = 4;
            this.lblPort.Text = "使用ポート番号：";
            // 
            // lblLOGsavePath
            // 
            this.lblLOGsavePath.AutoSize = true;
            this.lblLOGsavePath.Location = new System.Drawing.Point(24, 101);
            this.lblLOGsavePath.Name = "lblLOGsavePath";
            this.lblLOGsavePath.Size = new System.Drawing.Size(70, 12);
            this.lblLOGsavePath.TabIndex = 4;
            this.lblLOGsavePath.Text = "保存フォルダ：";
            // 
            // lblFilename
            // 
            this.lblFilename.AutoSize = true;
            this.lblFilename.Enabled = false;
            this.lblFilename.Location = new System.Drawing.Point(19, 126);
            this.lblFilename.Name = "lblFilename";
            this.lblFilename.Size = new System.Drawing.Size(75, 12);
            this.lblFilename.TabIndex = 4;
            this.lblFilename.Text = "ログファイル名：";
            // 
            // lblLOGtimestamp
            // 
            this.lblLOGtimestamp.AutoSize = true;
            this.lblLOGtimestamp.Location = new System.Drawing.Point(11, 178);
            this.lblLOGtimestamp.Name = "lblLOGtimestamp";
            this.lblLOGtimestamp.Size = new System.Drawing.Size(83, 12);
            this.lblLOGtimestamp.TabIndex = 4;
            this.lblLOGtimestamp.Text = "時間情報付加：";
            // 
            // lblLOGtimeLoc
            // 
            this.lblLOGtimeLoc.AutoSize = true;
            this.lblLOGtimeLoc.Location = new System.Drawing.Point(35, 204);
            this.lblLOGtimeLoc.Name = "lblLOGtimeLoc";
            this.lblLOGtimeLoc.Size = new System.Drawing.Size(59, 12);
            this.lblLOGtimeLoc.TabIndex = 4;
            this.lblLOGtimeLoc.Text = "付加位置：";
            // 
            // lblLOGdelAuto
            // 
            this.lblLOGdelAuto.AutoSize = true;
            this.lblLOGdelAuto.Location = new System.Drawing.Point(35, 230);
            this.lblLOGdelAuto.Name = "lblLOGdelAuto";
            this.lblLOGdelAuto.Size = new System.Drawing.Size(59, 12);
            this.lblLOGdelAuto.TabIndex = 4;
            this.lblLOGdelAuto.Text = "自動削除：";
            // 
            // lblStartDelay
            // 
            this.lblStartDelay.AutoSize = true;
            this.lblStartDelay.Location = new System.Drawing.Point(12, 261);
            this.lblStartDelay.Name = "lblStartDelay";
            this.lblStartDelay.Size = new System.Drawing.Size(95, 12);
            this.lblStartDelay.TabIndex = 4;
            this.lblStartDelay.Text = "起動時遅延時間：";
            // 
            // cmbSaveLength
            // 
            this.cmbSaveLength.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.cmbSaveLength.FormattingEnabled = true;
            this.cmbSaveLength.Items.AddRange(new object[] {
            "全て残す",
            "1日",
            "30日",
            "90日",
            "180日",
            "360日"});
            this.cmbSaveLength.Location = new System.Drawing.Point(96, 149);
            this.cmbSaveLength.Name = "cmbSaveLength";
            this.cmbSaveLength.Size = new System.Drawing.Size(70, 20);
            this.cmbSaveLength.TabIndex = 2;
            // 
            // lblSaveLength
            // 
            this.lblSaveLength.AutoSize = true;
            this.lblSaveLength.Location = new System.Drawing.Point(35, 152);
            this.lblSaveLength.Name = "lblSaveLength";
            this.lblSaveLength.Size = new System.Drawing.Size(59, 12);
            this.lblSaveLength.TabIndex = 4;
            this.lblSaveLength.Text = "保存期間：";
            // 
            // frmSettings
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(347, 321);
            this.Controls.Add(this.lblStartDelay);
            this.Controls.Add(this.lblLOGdelAuto);
            this.Controls.Add(this.lblLOGtimeLoc);
            this.Controls.Add(this.lblSaveLength);
            this.Controls.Add(this.lblLOGtimestamp);
            this.Controls.Add(this.lblFilename);
            this.Controls.Add(this.lblLOGsavePath);
            this.Controls.Add(this.lblPort);
            this.Controls.Add(this.lblPLC_IP);
            this.Controls.Add(this.chbDelayOn);
            this.Controls.Add(this.cmbLOGdelAuto);
            this.Controls.Add(this.cmbLOGtimeLoc);
            this.Controls.Add(this.cmbSaveLength);
            this.Controls.Add(this.cmbLOGtimeInfo);
            this.Controls.Add(this.txtFilename);
            this.Controls.Add(this.txtLOGpath);
            this.Controls.Add(this.txtStartDeray);
            this.Controls.Add(this.txtPort);
            this.Controls.Add(this.txtPLC_IP);
            this.Controls.Add(this.btnCancel);
            this.Controls.Add(this.btnSave);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedDialog;
            this.MaximizeBox = false;
            this.MinimizeBox = false;
            this.Name = "frmSettings";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterParent;
            this.Text = "設定画面";
            this.Load += new System.EventHandler(this.frmSettings_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button btnSave;
        private System.Windows.Forms.Button btnCancel;
        private System.Windows.Forms.TextBox txtPLC_IP;
        private System.Windows.Forms.TextBox txtPort;
        private System.Windows.Forms.TextBox txtLOGpath;
        private System.Windows.Forms.ComboBox cmbLOGtimeInfo;
        private System.Windows.Forms.ComboBox cmbLOGtimeLoc;
        private System.Windows.Forms.ComboBox cmbLOGdelAuto;
        private System.Windows.Forms.TextBox txtStartDeray;
        private System.Windows.Forms.CheckBox chbDelayOn;
        private System.Windows.Forms.TextBox txtFilename;
        private System.Windows.Forms.Label lblPLC_IP;
        private System.Windows.Forms.Label lblPort;
        private System.Windows.Forms.Label lblLOGsavePath;
        private System.Windows.Forms.Label lblFilename;
        private System.Windows.Forms.Label lblLOGtimestamp;
        private System.Windows.Forms.Label lblLOGtimeLoc;
        private System.Windows.Forms.Label lblLOGdelAuto;
        private System.Windows.Forms.Label lblStartDelay;
        private System.Windows.Forms.ComboBox cmbSaveLength;
        private System.Windows.Forms.Label lblSaveLength;
    }
}