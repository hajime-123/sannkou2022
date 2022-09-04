# %%
import mysql.connector as mydb
import datetime

todaydetail = datetime.datetime.today()
todaydetail_str=todaydetail.strftime('%Y%m%d')
#todaydetail_str2=todaydetail.strftime('%Y-%m-%d')

# コネクションの作成
conn = mydb.connect(
    host='127.0.0.1',
    port='3306',
    user='root',
    password='testneg',
    database='mat_db'
)
cur = conn.cursor()

tablename='trig05_'+todaydetail_str
sql_1 = 'insert into '+tablename
sql_2 = '(time,rotate1,rotate2,rotate3) values (%s,%s,%s,%s)'
sql_3 = sql_1+sql_2

#trig05_20211207
#"2020-04-01 08:30:00.29"


data = (todaydetail,1,1,1)
#data = (1,1)
#data = (1,)
 
#cur.execute(sql % data)
cur.execute(sql_3,data)
#cur.execute(sql,(todaydetail, 3, ))
#cur.execute(sql)
conn.commit()
cur.close()
conn.close()
# %%
