namespace WinFormsApp1
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
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
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.cul_button = new System.Windows.Forms.Button();
            this.hellolabel = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.textBox1 = new System.Windows.Forms.TextBox();
            this.textBox2 = new System.Windows.Forms.TextBox();
            this.read_button = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // cul_button
            // 
            this.cul_button.Location = new System.Drawing.Point(339, 224);
            this.cul_button.Name = "cul_button";
            this.cul_button.Size = new System.Drawing.Size(94, 29);
            this.cul_button.TabIndex = 0;
            this.cul_button.Text = "計算";
            this.cul_button.UseVisualStyleBackColor = true;
            this.cul_button.Click += new System.EventHandler(this.cal_click);
            // 
            // hellolabel
            // 
            this.hellolabel.AutoSize = true;
            this.hellolabel.Location = new System.Drawing.Point(128, 95);
            this.hellolabel.Name = "hellolabel";
            this.hellolabel.Size = new System.Drawing.Size(65, 20);
            this.hellolabel.TabIndex = 1;
            this.hellolabel.Text = "CSV合計";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(128, 194);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(94, 20);
            this.label1.TabIndex = 2;
            this.label1.Text = "CSV合計×1.5";
            // 
            // textBox1
            // 
            this.textBox1.Location = new System.Drawing.Point(308, 88);
            this.textBox1.Name = "textBox1";
            this.textBox1.Size = new System.Drawing.Size(125, 27);
            this.textBox1.TabIndex = 3;
            // 
            // textBox2
            // 
            this.textBox2.Location = new System.Drawing.Point(308, 191);
            this.textBox2.Name = "textBox2";
            this.textBox2.Size = new System.Drawing.Size(125, 27);
            this.textBox2.TabIndex = 4;
            // 
            // read_button
            // 
            this.read_button.Location = new System.Drawing.Point(339, 121);
            this.read_button.Name = "read_button";
            this.read_button.Size = new System.Drawing.Size(94, 29);
            this.read_button.TabIndex = 5;
            this.read_button.Text = "読込";
            this.read_button.UseVisualStyleBackColor = true;
            this.read_button.Click += new System.EventHandler(this.read_click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 20F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(553, 450);
            this.Controls.Add(this.read_button);
            this.Controls.Add(this.textBox2);
            this.Controls.Add(this.textBox1);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.hellolabel);
            this.Controls.Add(this.cul_button);
            this.Name = "Form1";
            this.Text = "Form1";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private Button cul_button;
        private Label hellolabel;
        private Label label1;
        private TextBox textBox1;
        private TextBox textBox2;
        private Button read_button;
    }
}