# drw作業１

pipが使えなくなったのでhttps://qiita.com/yasthon/items/954dc1aef9752838a0f0
を参考にpipを入れなおした

![1](drw作業画像1/1.PNG)

https://github.com/hajime-123/pythonsetup/blob/main/pythonsetup/python%E8%A8%AD%E5%AE%9A.md

以上のサイトのプログラムを実行。ライブラリをダウンロード

![1](drw作業画像1/2.PNG)


```
jupyter notebook
```
上記のコマンドでjupyterが使用できる。

画像表示がおかしかった。
バージョンのせい？

![1](drw作業画像1/3.PNG)

以前は3.4.1だったのでバージョンを変更してみる

```
pip uninstall matplotlib
pip install matplotlib==3.4.1
```



vscodeのjupyterのデバッグで動かすとおかしくなるみたい
pythonデバックで動かすと問題なかった


![1](drw作業画像1/4.PNG)


# mysqlをインストールする
まずは隠しフォルダを表示する

![1](drw作業画像1/5.PNG)

C:\ProgramData\MySQL\MySQL Server 8.0\Data

以上を作成するこれでディレクトリを選択できる

![1](drw作業画像1/6.PNG)

またE:\mysql\data、E:\mysql\programも作っておく

![1](drw作業画像1/8.PNG)

mysqlをインストールする

![1](drw作業画像1/7.PNG)

![1](drw作業画像1/9.PNG)

プログラムの保存先とデータの保存先の指定

![1](drw作業画像1/10.PNG)

確認がある

![1](drw作業画像1/11.PNG)

serverを選択してexcuteを押す　c++を入れる

![1](drw作業画像1/12.PNG)

なぜかいろいろ選択されてしまった。serverだけでよかったがとりあえずインストールする

![1](drw作業画像1/13.PNG)

![1](drw作業画像1/14.PNG)

![1](drw作業画像1/15.PNG)

![1](drw作業画像1/16.PNG)

![1](drw作業画像1/17.PNG)

![1](drw作業画像1/18.PNG)

![1](drw作業画像1/19.PNG)

![1](drw作業画像1/20.PNG)

![1](drw作業画像1/21.PNG)

![1](drw作業画像1/22.PNG)

パスを通す

![1](drw作業画像1/23.PNG)

保存先がどこになっているか確認

![1](drw作業画像1/24.PNG)

C:\ProgramData\MySQL\MySQL Server 8.0\my.ini

```
datadir=C:/ProgramData/MySQL/MySQL Server 8.0\Data
datadir=E:/mysql/data
```

![1](drw作業画像1/25.PNG)

コマンドプロンプトで下記を打つ

```
mysql -u root -p
show databases;
show variables like 'datadir'
exit
```

![1](drw作業画像1/26.PNG)

保存場所が変わっていなったのでサービス再起動

最初にデータ移動

![1](drw作業画像1/27.PNG)

![1](drw作業画像1/28.PNG)

サービス再起動

![1](drw作業画像1/29.PNG)

無事データ保存先を変更できた

![1](drw作業画像1/30.PNG)


