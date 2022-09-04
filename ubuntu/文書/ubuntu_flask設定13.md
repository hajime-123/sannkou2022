## ubuntuのflask設定方法13

### PLCに対してPC（ubuntu)からアクセスできるか確認

まずはpingでアクセスできるか確認

```
ping 172.24.11.95
```

![1](ubuntu_flask設定画像13/1.PNG)

workフォルダとsaveフォルダを作る

![1](ubuntu_flask設定画像13/2.PNG)

workフォルダとsaveフォルダの中身

![1](ubuntu_flask設定画像13/3.PNG)

mat_collsub.pyでひとまずデータとれるか確認する。

![1](ubuntu_flask設定画像13/4.PNG)

エラーが出ていた。

262番目にエラーが出たようだがわかりにくいのでsys.exc_info()を追加した

![1](ubuntu_flask設定画像13/5.PNG)

IndexError('string index out of range')

範囲外？

正常な時の文字数は3622だった

![1](ubuntu_flask設定画像13/6.PNG)

異常時は1072個（262個）しかデータが帰ってきていなかった？

もしくは2144個（530個）の時もあった

デスクトップではうまくいくが、ノートパソコンだとうまくいかなかった。性能の違い？

![1](ubuntu_flask設定画像13/7.PNG)

しょうがないので一度に900（実際の振動データは800個）取るのではなく200個ずつにした

![1](ubuntu_flask設定画像13/8.PNG)

![1](ubuntu_flask設定画像13/9.PNG)

![1](ubuntu_flask設定画像13/10.PNG)

CSVも比較してみる

![1](ubuntu_flask設定画像13/11.PNG)

![1](ubuntu_flask設定画像13/12.PNG)

### PLCのデータをCSVとDBに保存

まずはテーブルを作ってみた。

またCSVを自動生成するところにも日にちが変化していたらテーブル作るようにした

![1](ubuntu_flask設定画像13/13.PNG)

![1](ubuntu_flask設定画像13/14.PNG)

急にPCとリモート接続できなくなったが無線接続されていた

次に実際にテーブル内にデータを入れてみる

![1](ubuntu_flask設定画像13/15.PNG)

値は取れているけど時間や値がすべて小数点以下が取れていなかった

![1](ubuntu_flask設定画像13/16.PNG)

一部修正

![1](ubuntu_flask設定画像13/17.PNG)

値確認。OKだった

![1](ubuntu_flask設定画像13/18.PNG)

mat_collmain.pyで動かしてもOKそうだったので

その他のテーブルも作る。コミットは毎回するのではなくまとめて行う

テストとして振動用のテーブルだけ作ってみる

dbtable_crate_3.py

```python

#%%
import mysql.connector as mydb
import datetime

todaydetail = datetime.datetime.today()
todaydetail_str=todaydetail.strftime('%Y%m%d')

# コネクションの作成
conn = mydb.connect(
    host='127.0.0.1',
    port='3306',
    user='test',
    password='tkroyc123',
    database='test_database'
)

conn.ping(reconnect=True)
print(conn.is_connected())

cur = conn.cursor()

strage=[]
for i in range(1,801):
    v='id'+str(i)+' int'
    w=i
    strage.append(v)

strage2=[]
for i in range(1,802):
    W='?'
    strage2.append(W)

mojiretsu=','.join(strage)
mojiretsu2=','.join(strage2)    

sql ="CREATE TABLE %s ( `id` int NOT NULL AUTO_INCREMENT,`time` datetime(1) DEFAULT NULL,"
sql2=mojiretsu
sql3=",PRIMARY KEY (`id`))" 
sql_all=sql+sql2+sql3
dbname='trig600vib_'+todaydetail_str
#dbname='test_tabe_20210820'
cur.execute(sql_all % dbname)
#cur.execute(sql,('test3'))
#cur.execute(sql,('test3'))
conn.commit()

cur.close()
conn.close()

# %%

```

問題なくテーブル作成できていた。

![1](ubuntu_flask設定画像13/19.PNG)

dbeaverで前のｄｂを確認できるようにした

![1](ubuntu_flask設定画像13/20.PNG)

以上をダウンロード。ドライバの編集で先ほどのファイルを読むようにする。

![1](ubuntu_flask設定画像13/21.PNG)

![1](ubuntu_flask設定画像13/22.PNG)

![1](ubuntu_flask設定画像13/23.PNG)

今回テーブルを新たに4個作る時はおおよそ0.3秒程度かかる

![1](ubuntu_flask設定画像13/24.PNG)

新たに4個作るらなくていい場合はおおよそ0.03秒程度

また、CSV、ｄｂにデータをすべて入れる場合も0.1秒程度かかる

![1](ubuntu_flask設定画像13/25.PNG)

もし処理に時間がかかった場合を想定してタイムスリープを入れたところ１秒ごとの収集になった。

![1](ubuntu_flask設定画像13/26.PNG)













































