### csharpの設定方法

PLCのデータを収集するコンソールアプリケーションを作ってみる。

まずはCSVに吐き出すプログラムを記載

![1](csharp画像4/1.PNG)

```c#
using System.Text;
```

これを記載することでEncoding.UTF8が使用できるようになる。

実行させてみた。

![1](csharp画像4/2.PNG)

無事にCSVが出力された。

次にPLCとの通信プログラムを作っていく。

まずはPLCの設定を確認する。

![1](csharp画像4/3.PNG)

IP　172.21.5.100 ポート　8888

バイナリコード通信ということが分かった。

次にC＃のプログラムを作成する。

![1](csharp画像4/4.PNG)

ソケット通信するためのライブラリ読込

送信用の電文をbyteにする関数を作成。

Byte配列 => 16進数文字列の関数作成。

16進数文字列 => 符号付き数値関数の作成。

https://webbibouroku.com/Blog/Article/byte-hex

https://takap-tech.com/entry/2020/07/09/002557

参照

![1](csharp画像4/5.PNG)

![1](csharp画像4/6.PNG)

とりあえず作った。

https://momomo-97.com/vb-net-mc-protocol-read-write-commands/#toc7

https://momomo-97.com/communicate-with-mitsubishi-plc-using-vb-net-mc-protocol/

参照

返信された電文の中身を確認する。

![1](csharp画像4/7.PNG)

ちゃんと返信が返ってきた。

電文を符号付き数値として出力できるようにプログラム修正。

![1](csharp画像4/8.PNG)

![1](csharp画像4/9.PNG)

実行してみた。

![1](csharp画像4/10.PNG)

符号付き数値として出力することができた。







