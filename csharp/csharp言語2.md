### csharpの設定方法

フォームアプリケーションを作ってみる。プロジェクトを作成

windowsフォームアプリケーション開発を選択

![1](csharp画像2/1.PNG)

プロジェクト名と保存場所を決める。

![1](csharp画像2/2.PNG)

フレームワークの選択

![1](csharp画像2/3.PNG)

作成を押すと下記画面が現れる

![1](csharp画像2/4.PNG)

名前を付けて保存。上書き保存する。

初期段階のコード　フォーム用　（Form1.Designer.cs）

![1](csharp画像2/5.PNG)

初期段階のコード　プログラム用（Program.cs）

![1](csharp画像2/6.PNG)

流れとしてはprogram.csが実行されて、form1.csが実行されるという流れになる。

まずはこの状態で実行してみる。

![1](csharp画像2/7.PNG)

ウィンドウフォーム画面が出た。

![1](csharp画像2/8.PNG)

また、実行ファイルが作成されたのも確認できた。

ボタンを配置してみる

![1](csharp画像2/9.PNG)

Form1.Designer.csにプログラムが追記された。

![1](csharp画像2/10.PNG)

form1のボタンを選択した状態でプロパティを確認し、nameをhellobuttonにする。

![1](csharp画像2/11.PNG)

ラベルを貼り付け、nameをhellolabelにする

![1](csharp画像2/12.PNG)

button1を選択した状態でイベントタブを選択しhellobuttonclickと打つ

![1](csharp画像2/13.PNG)

form1.csにprivate void hellobuttonclick(object sender, EventArgs e)という関数が生成された。

![1](csharp画像2/14.PNG)

ボタンクリックするとラベルがhelloworldになるアプリができた。

![1](csharp画像2/15.PNG)






