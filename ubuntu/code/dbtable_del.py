# %%
import mysql.connector as mydb
import datetime
import pandas as pd

# コネクションの作成
conn = mydb.connect(
    host='127.0.0.1',
    port='3306',
    user='root',
    password='testneg',
    database='mat_db'
)

cur = conn.cursor()

sql ="show tables like 'trig05_%'"
cur.execute(sql)
rows = cur.fetchall()

df = pd.DataFrame(rows)
print(df.iloc[0,0])
print(len(df))
if len(df)>5:
    print(print(df.iloc[0,0]))
    sql ="drop table if exists %s"
    cur.execute(sql % df.iloc[0,0])
    conn.commit()
	#cur.close()
	#conn.close()
conn.commit()
cur.close()
conn.close()    
# %%
