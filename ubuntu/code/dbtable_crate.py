# %%
import mysql.connector as mydb
import datetime

todaydetail = datetime.datetime.today()
todaydetail_str=todaydetail.strftime('%Y%m%d')

# コネクションの作成
conn = mydb.connect(
    host='127.0.0.1',
    port='3306',
    user='root',
    password='testneg',
    database='mat_db'
)

#conn.ping(reconnect=True)
#print(conn.is_connected())
import mysql.connector as mydb
import datetime

todaydetail = datetime.datetime.today()
todaydetail_str=todaydetail.strftime('%Y%m%d')

# コネクションの作成
conn = mydb.connect(
    host='127.0.0.1',
    port='3306',
    user='root',
    password='testneg',
    database='mat_db'
)

#conn.ping(reconnect=True)
#print(conn.is_connected())
cur = conn.cursor()
sql ="CREATE TABLE %s (\
  `id` int NOT NULL AUTO_INCREMENT,\
  `time` datetime NOT NULL,\
  `rotate1` int DEFAULT NULL,\
  `rotate2` int DEFAULT NULL,\
  `rotate3` int DEFAULT NULL,\
  PRIMARY KEY (`id`))"

tablename='trig05_'+todaydetail_str
#tablename='trig05_20210905'
cur.execute(sql % tablename)
conn.commit()
cur.close()
conn.close()
# %%
