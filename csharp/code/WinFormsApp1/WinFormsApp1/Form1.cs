namespace WinFormsApp1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void read_click(object sender, EventArgs e)
        {
            StreamReader sr = new StreamReader(@"data/test.csv");
            List<int> sum_list = new List<int>();
            int sum = 0;
            // �����܂ŌJ��Ԃ�
            while (!sr.EndOfStream)
            {
                // CSV�t�@�C���̈�s��ǂݍ���
                string line = sr.ReadLine();
                // �ǂݍ��񂾈�s���J���}���ɕ����Ĕz��Ɋi�[����
                string[] values = line.Split(',');

                // �z�񂩂烊�X�g�Ɋi�[����
                List<string> lists = new List<string>();
                //List<int> lists = new List<int>();
                lists.AddRange(values);

                // �R���\�[���ɏo�͂���
                foreach (string list in lists)
                {
                    System.Console.Write("{0} ", list);
                    sum_list.Add(int.Parse(list));
                }
                //Console.WriteLine(sum_list);
                System.Console.WriteLine();
            }
            //Console.WriteLine(sum_list);
            for (int i = 0; i < sum_list.Count; i++)
            {
                sum += sum_list[i];
            }

            this.textBox1.Text = sum.ToString();

        }

        private void cal_click(object sender, EventArgs e)
        {
            int num= int.Parse(this.textBox1.Text);
            float num2 = (float)num;
            float FloatTest = 0.0f;
            FloatTest = num2 * (1.5f);
            this.textBox2.Text = FloatTest.ToString();

        }
    }
}