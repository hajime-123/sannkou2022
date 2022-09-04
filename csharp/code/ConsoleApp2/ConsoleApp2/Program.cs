// See https://aka.ms/new-console-template for more information
//Console.WriteLine("Hello, World!");
using System;
using System.Text;
using System.IO;
using System.Net;
using System.Net.Sockets;
using System.Collections.Generic;
using System.Linq;

class Test
{
    // 16進数文字列 => Byte配列
    public static byte[] StringToBytes(string str)
    {
        var bs = new List<byte>();
        for (int i = 0; i < str.Length / 2; i++)
        {
            bs.Add(Convert.ToByte(str.Substring(i * 2, 2), 16));
        }
        // "01-AB-EF" こういう"-"区切りを想定する場合は以下のようにする
        // var bs = str.Split('-').Select(hex => Convert.ToByte(hex, 16));
        return bs.ToArray();
    }

    // Byte配列 => 16進数文字列
    public static string BytesToString(byte[] bs)
    {
        var str = BitConverter.ToString(bs);
        // "-"がいらないなら消しておく
        str = str.Replace("-", string.Empty);
        return str;
    }

    // 16進数文字列 => 符号付き数値
    public static int StringToint(string moji, int num)
    {
        var str1 = moji.Substring((num - 1) * 8 + 22, 2);
        var str2 = moji.Substring((num - 1) * 8 + 22 + 2, 2);
        var str3 = moji.Substring((num - 1) * 8 + 22 + 4, 2);
        var str4 = moji.Substring((num - 1) * 8 + 22 + 6, 2);
        var str_all = str4 + str3 + str2 + str1;
        int num1 = Convert.ToInt32(str_all, 16);
        // "-"がいらないなら消しておく

        return num1;
    }
        static void Main()
    {
        //string faile = @"mydata2.csv";
        //float[] box = {10f,11f,12f,13f,14f,15f,16f,17f };
        //StreamWriter sw = new StreamWriter(faile, false, Encoding.UTF8);
        //for (int i = 0; i < box.Length; i += 1)
        //{
        //    sw.Write(box[i]);
        //    sw.Write(",");
        //}
        //sw.Close();

        try
        {
            IPAddress host1 = IPAddress.Parse("172.21.5.100");
            int port1 = 8888;
            IPEndPoint ipe1 = new IPEndPoint(host1, port1);
            //ソケット作成
            Socket socket = new Socket(host1.AddressFamily, SocketType.Stream, ProtocolType.Tcp);

            socket.Connect(ipe1);
            Console.WriteLine("接続成功");

            //Sendで送信
            //D9000から1個データ収集　ダブル
            //string plc_send1 = "500000FFFF03000C00100001040000282300A82C01";
            string plc_send1;
            string plc_send1_0 = "50";
            string plc_send1_1 = "00";
            string plc_send1_2 = "00";// 'ネットワーク番号
            string plc_send1_3 = "FF";//PC番号
            string plc_send1_4 = "FF";//要求先ユニットI/O番号
            string plc_send1_5 = "03";//要求先ユニットI/O番号
            string plc_send1_6 = "00";//要求先ユニット局番号
            string plc_send1_7 = "0C";//要求データ長(監視タイマ+要求データの要素数：12)
            string plc_send1_8 = "00";//要求データ長(監視タイマ+要求データの要素数：12)
            string plc_send1_9 = "10";//監視タイマ(2Byte)
            string plc_send1_10 = "00";//監視タイマ(2Byte)
            string plc_send1_11 = "01";//コマンド 読取(0401)
            string plc_send1_12 = "04";//コマンド 読取(0401)
            string plc_send1_13 = "00";//サブコマンド ワード(0000)
            string plc_send1_14 = "00";//サブコマンド ワード(0000)
            string plc_send1_15 = "28";//デバイス番号(D9000)
            string plc_send1_16 = "23";//デバイス番号(D9000)
            string plc_send1_17 = "00";//デバイス番号(D9000)
            string plc_send1_18 = "A8";//デバイスコード
            string plc_send1_19 = "2C";//読取点数(300)
            string plc_send1_20 = "01";//読取点数(300)

            plc_send1 = plc_send1_0 + plc_send1_1 + plc_send1_2 + plc_send1_3 + plc_send1_4 + plc_send1_5 +
                plc_send1_6 + plc_send1_7 + plc_send1_8 + plc_send1_9 + plc_send1_10 + plc_send1_11 +
                 plc_send1_12 + plc_send1_13 + plc_send1_14 + plc_send1_15 + plc_send1_16 + plc_send1_17 +
                  plc_send1_18 + plc_send1_19 + plc_send1_20;



                //バイナリ変換
                // 16進数文字列 => Byte配列
                var bytes = StringToBytes(plc_send1);

            Console.WriteLine(bytes);
            //送信
            socket.Send(bytes, bytes.GetLength(0), SocketFlags.None);
            Console.WriteLine("送信");
            //Receiveで受信している。
            byte[] bytes2 = new byte[1024];
            
            int bytesRec = socket.Receive(bytes2);
            //string data = Encoding.UTF8.GetString(bytes2, 0, bytesRec);
            //Console.WriteLine(data);
            // Byte配列 => 16進数文字列
            var hexString = BytesToString(bytes2);
            Console.WriteLine(hexString);
            Console.WriteLine("test");
            Console.WriteLine(hexString.Substring(30,8));
            Console.WriteLine("test2");
            int plc_return1 = StringToint(hexString, 1);
            Console.WriteLine(plc_return1);


            //string data2 = bytesRec(11);


                //ソケットを終了している。
            socket.Shutdown(SocketShutdown.Both);
            socket.Close();
            Console.WriteLine("接続終了");
        }
        catch (Exception ex)
        {
            Console.WriteLine(ex.Message);
        }
    }

}

