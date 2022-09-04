## ubuntuのflask設定方法3

### mysqlの設定等

MySQLにログイン

```
sudo mysql -u root
```

データベース一覧表示

```
show databases;
```

![1](ubuntu_flask設定画像2/1.PNG)

テストデータベース作成

```
create database test_database; 
```

テストデータベースにテストテーブル作成

```
create table test_database.test_table (id int, total_pix int, primary key (id)); 
```

使用するDBに移動

```
use test_database
```

![1](ubuntu_flask設定画像2/2.PNG)

テストテーブルにデータ投入

```
insert into test_database.test_table(id, total_pix) values(58, 2054); #DBに移動してない時
insert into test_table(id, total_pix) values(58, 2054); 
```

テストテーブル表示

```
select * from test_database.test_table;
```

![1](ubuntu_flask設定画像2/3.PNG)

テストデータベース削除

```
drop database test_database;
```

ログアウト

```
exit
```

データの保存場所確認

![1](ubuntu_flask設定画像2/4.PNG)

ルートユーザーで中身を確認

```
sudo su - 
cd /var/lib/mysql/
```

![1](ubuntu_flask設定画像2/5.PNG)

ルートユーザーで中身の容量を確認

```
du -h /var/lib/mysql/
```

![1](ubuntu_flask設定画像3/1.PNG)



### dbeaverの設定

#### インストール

```
sudo snap install dbeaver-ce
```

ラズパイの場合

```
sudo apt update
sudo apt install snapd
sudo reboot
sudo snap install core
sudo snap install dbeaver-ce
```

![1](ubuntu_flask設定画像3/2.PNG)

#### mysql接続

データベースをクリック

![1](ubuntu_flask設定画像3/3.PNG)

新しい接続をクリック

![1](ubuntu_flask設定画像3/4.PNG)

必要事項を記載

![1](ubuntu_flask設定画像3/5.PNG)

ドライバが必要

![1](ubuntu_flask設定画像3/6.PNG)

ドライバをダウンロード

![1](ubuntu_flask設定画像3/7.PNG)

接続しようとしたらうまくいかなかった

![1](ubuntu_flask設定画像3/8.PNG)

そういえばユーザー作っていなかった。MySQLのユーザ一覧を確認

```
sudo mysql -u root -p
SELECT  host, user FROM mysql.user;
```

![1](ubuntu_flask設定画像3/9.PNG)

```
sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf
```

![1](ubuntu_flask設定画像3/10.PNG)

設定反映　

```
sudo systemctl restart mysql
```

接続できなかったのでrootにパスワードをつけてみた

```
sudo mysql -u root
use mysql;
update mysql.user set password=password('tkroyc123') where user = 'root';#この書き方は古い
set password for 'root'@'localhost' = 'tkroyc123';#mysql8からはこっち
flush privileges;#設定反映
```

これでもうまくいかなかったので別ユーザーを作ることにした。

```
grant all privileges on *.* to test@"%" identified by 'tkroyc123' with grant option;
select user,host from mysql.user;
SHOW GRANTS;
exit
sudo systemctl restart mysql
```



```
CREATE USER 'test'@'%' IDENTIFIED BY 'tkroyc123';
```

怒られた　上だけでもOKだった

```
set global validate_password.policy = "LOW";
set global validate_password.special_char_count = 0;
```

testユーザーを作った

```
CREATE USER 'test'@'%' IDENTIFIED BY 'tkroyc123';
GRANT ALL PRIVILEGES ON *.* TO 'test'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;
```

![1](ubuntu_flask設定画像3/11.PNG)

接続しようとしたらうまくいかなかった

![1](ubuntu_flask設定画像3/12.PNG)

JDBCドライバのプロパティ「allowPublicKeyRetrieval」をtrue、「useSSL」をfalseにする

![1](ubuntu_flask設定画像3/13.PNG)

![1](ubuntu_flask設定画像3/14.PNG)

#### テーブル操作

カラムを追加する

![1](ubuntu_flask設定画像3/15.PNG)

insert_timeを作ってみた

![1](ubuntu_flask設定画像3/16.PNG)

saveボタンを押す

![1](ubuntu_flask設定画像3/17.PNG)

最終的に下記のようにした

![1](ubuntu_flask設定画像3/18.PNG)



### pythonでmysqlを操作する

まずはpythonで触れるようにライブラリインストール

```
pip3 install mysql-connector-python
```

mysql_test　値を入れてみる

mysql_test.py

```
import mysql.connector as mydb

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

sql ='insert into test_table (insert_time, total_pix) values ("2020-04-01 08:30:00",100)'
cur.execute(sql)
conn.commit()

cur.close()
conn.close()
```

値が入ったことを確認できた

![1](ubuntu_flask設定画像3/19.PNG)

ちょっと変えてみた

```
import mysql.connector as mydb
import time
import datetime

todaydetail = datetime.datetime.today()
start = time.time()
todaydetail_str=str(todaydetail)
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

sql ='insert into test_table_1 (insert_time, total_pix) values (%s, %s)'
cur.execute(sql, (todaydetail, 3, ))
conn.commit()

cur.close()
conn.close()
```

test_table_1を作って小数点も１個表示できるようにした

![1](ubuntu_flask設定画像3/21.PNG)



![1](ubuntu_flask設定画像3/22.PNG)

#### 大量データをテーブルに追加

test_databaseと各テーブルの状況を確認

![1](ubuntu_flask設定画像3/23.PNG)



mysql_test_for.py

```
import mysql.connector as mydb


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

for i in range(10000):
    sql ='insert into test_table_1 (insert_time, total_pix) values ("2020-04-01 08:30:00",100)'
    cur.execute(sql)
    conn.commit()

cur.close()
conn.close()
```

データベース容量の確認

```
use test_database;
select table_schema, sum(data_length+index_length) /1024 /1024 as MB from information_schema.tables where table_schema = database();

select table_schema, sum(data_length+index_length) /1024 /1024 as MB from information_schema.tables  group by table_schema order by sum(data_length+index_length) desc;

```

![1](ubuntu_flask設定画像3/24.PNG)

テーブル

```
SELECT table_name, round(((data_length + index_length) / 1024), 2) AS MB FROM information_schema.TABLES WHERE table_schema = database();

select  
table_name, engine, table_rows as tbl_rows, avg_row_length as rlen,  
floor((data_length+index_length)/1024/1024) as allMB,  #総容量
floor((data_length)/1024/1024) as dMB,  #データ容量
floor((index_length)/1024/1024) as iMB   #インデックス容量
from information_schema.tables  
where table_schema=database()  
order by (data_length+index_length) desc; 
```

![1](ubuntu_flask設定画像3/25.PNG)

下記の書き方もある。

```
use test_database;
select 
table_name, engine, table_rows as tbl_rows, avg_row_length as rlen, 
floor((data_length+index_length)/1024) as allMB, #総容量
floor((data_length)/1024) as dMB, #データ容量
floor((index_length)/1024) as iMB #インデックス容量
from information_schema.tables 
where table_schema=database() 
order by (data_length+index_length) desc;
```

別のデータの見方　前回よりデータが大きくなっている

![1](ubuntu_flask設定画像3/26.PNG)

```
sudo su - 
cd /var/lib/mysql/test_database
du -h /var/lib/mysql/test_database
ls -l
```

![1](ubuntu_flask設定画像3/27.PNG)

これでもデータを確認することができた。

またテーブルを消すことでデータベースの容量が小さくなっていることも分かった。

