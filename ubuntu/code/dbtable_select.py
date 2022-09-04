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
cur = conn.cursor()

tablename='trig05_'+todaydetail_str
sql_1 = 'select time,rotate1,rotate2,rotate3 from '+tablename
sql_2 = ' order by id desc limit %s'
sql_3 = sql_1+sql_2

data = (5,)
cur.execute(sql_3,data)
result_g = cur.fetchall()
cur.close()
conn.close()

print(result_g[0][0])
# %%
