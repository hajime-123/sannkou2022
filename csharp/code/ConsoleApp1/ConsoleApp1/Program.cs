// See https://aka.ms/new-console-template for more information
using System;
using System.IO;

//Console.WriteLine("Hello, World!");
//Console.ReadLine();


//namespace CsvRead
//{
//    class Test
//    {
//        static void Main()
//        {
//            // 読み込みたいCSVファイルのパスを指定して開く
//            StreamReader sr = new StreamReader(@"test.csv");
//            {
//                // 末尾まで繰り返す
//                while (!sr.EndOfStream)
//                {
//                    // CSVファイルの一行を読み込む
//                    string line = sr.ReadLine();
//                    // 読み込んだ一行をカンマ毎に分けて配列に格納する
//                    string[] values = line.Split(',');

//                    // 配列からリストに格納する
//                    List<string> lists = new List<string>();
//                    lists.AddRange(values);

//                    // コンソールに出力する
//                    foreach (string list in lists)
//                    {
//                        System.Console.Write("{0} ", list);
//                    }
//                    System.Console.WriteLine();
//                }
//                System.Console.ReadKey();
//            }
//        }
//    }
//}

class Test
{
    static void Main()
    {
        // 読み込みたいCSVファイルのパスを指定して開く
        //StreamReader sr = new StreamReader(@"../../test.csv");
        StreamReader sr = new StreamReader(@"data/test.csv");
        List<int> sum_list = new List<int>();
        int sum=0;
        // 末尾まで繰り返す
        while (!sr.EndOfStream)
        {
            // CSVファイルの一行を読み込む
            string line = sr.ReadLine();
            // 読み込んだ一行をカンマ毎に分けて配列に格納する
            string[] values = line.Split(',');

            // 配列からリストに格納する
            List<string> lists = new List<string>();
            //List<int> lists = new List<int>();
            lists.AddRange(values);

            // コンソールに出力する
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
        System.Console.WriteLine(sum);
        System.Console.WriteLine();
        System.Console.ReadKey();

    }
}
