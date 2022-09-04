### csharpの設定方法

フォームアプリケーションを作ってみる。

CSVを読み込んで計算するアプリを作ってみる。

画面構成は以下のようにした

![1](csharp画像3/1.PNG)

その時のForm1.Designer.cs

![1](csharp画像3/2.PNG)

それぞれのボタンに関数を記載していく。

イベントタブに名称を記載する。read_click

![1](csharp画像3/3.PNG)

cal_click

![1](csharp画像3/4.PNG)

Form1.cs

![1](csharp画像3/5.PNG)

private void hellobuttonclick(object sender, EventArgs e)は無くなったので消しておく。

読込ボタンを押してCSVデータが読み取れるように関数を記載する。

![1](csharp画像3/6.PNG)

またdataフォルダにtest.csvを保存した。このデータを読む

![1](csharp画像3/7.PNG)

次に計算ボタンを押してCSVの合計値に1.5倍する関数を作る。

![1](csharp画像3/8.PNG)

```c#
private void cal_click(object sender, EventArgs e)
{
    int num= int.Parse(this.textBox1.Text);
    float num2 = (float)num;
    float FloatTest = 0.0f;
    FloatTest = num2 * (1.5f);
    this.textBox2.Text = FloatTest.ToString();

}
```

実行させてみた。

![1](csharp画像3/9.PNG)


CSVの読み取り、計算すべて実行することができた。







