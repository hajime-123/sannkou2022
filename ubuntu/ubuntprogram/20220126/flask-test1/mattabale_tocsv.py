#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#%%
#----------------

import csv
import datetime
import os
import datetime
import time
import sys
import mysql.connector as mydb
import pandas as pd
#(1)dbのテーブル名取得
conn = mydb.connect(
    host='127.0.0.1',
    port='3306',
    user='test',
    password='tkroyc123',
    database='mat_db'
)

sql="show tables like 'trig10%'"
sql2="show tables like 'trig05%'"
cur = conn.cursor()
cur.execute(sql)
#conn.commit()
result_g = cur.fetchall()
cur.execute(sql2)
result_g2 = cur.fetchall()
cur.close()
conn.close()

#(2)dbのテーブル名からディレクトリ作成
for i in range(len(result_g)-1):
    cwd="/home/haji/flask-test1/save2/1"
    cwd2="/home/haji/flask-test1/save2/4"
    dirname=result_g[i][0][-8:-2]
    new_dir_path=cwd+'/'+dirname
    new_dir_path2=cwd2+'/'+dirname
    os.makedirs(new_dir_path, exist_ok=True)
    os.makedirs(new_dir_path2, exist_ok=True)

    #(3)dbのテーブル名のCSVを作成
    try:
        conn = mydb.connect(
            host='127.0.0.1',
            port='3306',
            user='test',
            password='tkroyc123',
            database='mat_db'
        )
        cur = conn.cursor()
        sql_1="select 'id','time','meand1','meand2','meand3','flow1' union select * \
            from "+result_g[i][0]+" order by id desc"
        # sql_2="'"+new_dir_path+'/'+result_g[i][0]+".csv"+"' fields terminated by ','"
        # sql_3=""" OPTIONALLY ENCLOSED BY '"'"""
        sql=sql_1
        cur.execute(sql)
        result_table = cur.fetchall()
        cur.close()
        conn.close()
        df = pd.DataFrame(result_table)
        df.columns =df.iloc[0,:]
        df.index =df.iloc[:,0]
        df1=df.drop(df.index[[0]])
        df2=df1.drop(df.columns[[0]], axis=1)
        df3=df2.sort_values(by=["time"])
        df3.to_csv(new_dir_path+"/"+result_g[i][0]+".csv")
    except:
        print(sys.exc_info())
    finally:
        conn.close()

    try:
        conn = mydb.connect(
            host='127.0.0.1',
            port='3306',
            user='test',
            password='tkroyc123',
            database='mat_db'
        )
        cur = conn.cursor()
        sql_1="select 'id','time','rotate1','rotate2','rotate3' union select * \
            from "+result_g2[i][0]+" order by id desc"
        # sql_2="'"+new_dir_path2+'/'+result_g2[i][0]+".csv"+"' fields terminated by ','"
        # sql_3=""" OPTIONALLY ENCLOSED BY '"'"""
        sql=sql_1
        cur.execute(sql)
        result_table = cur.fetchall()
        cur.close()
        conn.close()
        df = pd.DataFrame(result_table)
        df.columns =df.iloc[0,:]
        df.index =df.iloc[:,0]
        df1=df.drop(df.index[[0]])
        df2=df1.drop(df.columns[[0]], axis=1)
        df3=df2.sort_values(by=["time"])
        df3.to_csv(new_dir_path2+"/"+result_g2[i][0]+".csv")
    except:
        print(sys.exc_info())
    finally:
        conn.close()


#if __name__ == '__main__':
    #func_600()
    #func_dbdel()









# %%



# %%
