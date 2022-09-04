#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#%%
#----------------


import time
import datetime
import csv
import socket

import os
import mysql.connector as mydb#220111
import sys

start=time.time()
plc_send1=str("500000FFFF03000C00100001040000307500A82C01")#D30000から300個データを取得　ダブルワード 20190726追加
plc_send2=str("500000FFFF03000C00100001040000701700A8C800")#D6000から200個データを取得　シングル
plc_send2_2=str("500000FFFF03000C00100001040000381800A8C800")#D6200から200個データを取得　シングル
plc_send2_3=str("500000FFFF03000C00100001040000001900A8C800")#D6400から200個データを取得　シングル
plc_send2_4=str("500000FFFF03000C00100001040000C81900A8C800")#D6600から200個データを取得　シングル
plc_send2_5=str("500000FFFF03000C00100001040000901A00A8C800")#D6800から200個データを取得　シングル
byte_data1=bytes.fromhex(plc_send1)
byte_data2=bytes.fromhex(plc_send2)
byte_data2_2=bytes.fromhex(plc_send2_2)
byte_data2_3=bytes.fromhex(plc_send2_3)
byte_data2_4=bytes.fromhex(plc_send2_4)
byte_data2_5=bytes.fromhex(plc_send2_5)
host = "172.24.11.95" #お使いのサーバーのホスト名を入れます
port = 5000 #適当なPORTを指定してあげます
def s32(value):return -(value & 0b10000000000000000000000000000000) | \
(value & 0b01111111111111111111111111111111)#0,1の数重要31個
def s16(value):return -(value & 0b1000000000000000) | (value & 0b0111111111111111)

joined_path_1='./work/1' #一時作業用のworkフォルダ1
joined_path_2='./work/2' #一時作業用のworkフォルダ60
joined_path_3='./work/3' #一時作業用のworkフォルダ設定
joined_path_4='./work/4' #一時作業用のworkフォルダ0.5
joined_path2_1='./save/1' #保存先フォルダ1
joined_path2_2='./save/2' #保存先フォルダ60
joined_path2_3='./save/3' #保存先フォルダ設定
joined_path2_4='./save/4' #保存先フォルダ0.5

strage=[]
for i in range(1,801):
    v='id'+str(i)+' int'
    w=i
    strage.append(v)

strage2=[]
for i in range(1,802):
    W='%s'
    strage2.append(W)

strage3=[]
for i in range(1,801):
    v='id'+str(i)
    strage3.append(v)
#print(box4) 
mojiretsu=','.join(strage)
mojiretsu2=','.join(strage2)
mojiretsu3=','.join(strage3)

mode='a'
#err_count=0
box=[0,0,0,0,0,0,0]
box_2=[0,0,0,0]
v1,v2,v3,v4,v5,v6,v7,v8,v9=0,0,0,0,0,0,0,0,0
box_1=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]#20190710追加20190726追加
w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12,w13,w14,w15,w16,w17,w18,w19,w20=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0#20190710追加20190726追加
err_count=0

todaydetail = datetime.datetime.today()
t1=todaydetail.strftime("%Y%m%d%H")
todaydetail_str=todaydetail.strftime('%Y%m%d')#211119
#tablename='trig05_'+todaydetail_str
#220111
try:
    # コネクションの作成
    conn = mydb.connect(
        host='127.0.0.1',
        port='3306',
        user='test',
        password='tkroyc123',
        database='mat_db'
    )
    cur = conn.cursor()
    sql ="CREATE TABLE %s (\
      `id` int NOT NULL AUTO_INCREMENT,\
      `time` datetime(1) NOT NULL,\
      `rotate1` float DEFAULT NULL,\
      `rotate2` float DEFAULT NULL,\
      `rotate3` float DEFAULT NULL,\
      PRIMARY KEY (`id`))"
    tablename05='trig05_'+todaydetail_str
    cur.execute(sql % tablename05)
    conn.commit()
    cur.close()
except:
    print(sys.exc_info())
finally:
    conn.close()

try:
    # コネクションの作成
    conn = mydb.connect(
        host='127.0.0.1',
        port='3306',
        user='test',
        password='tkroyc123',
        database='mat_db'
    )
    cur = conn.cursor()
    sql ="CREATE TABLE %s (\
      `id` int NOT NULL AUTO_INCREMENT,\
      `time` datetime(1) NOT NULL,\
      `meand1` float DEFAULT NULL,\
      `meand2` float DEFAULT NULL,\
      `meand3` float DEFAULT NULL,\
      `flow1` float DEFAULT NULL,\
      PRIMARY KEY (`id`))"
    tablename10='trig10_'+todaydetail_str
    cur.execute(sql % tablename10)
    conn.commit()
    cur.close()
except:
    print(sys.exc_info())
finally:
    conn.close()

try:
    # コネクションの作成
    conn = mydb.connect(
        host='127.0.0.1',
        port='3306',
        user='test',
        password='tkroyc123',
        database='mat_db'
    )
    cur = conn.cursor()
    sql ="CREATE TABLE %s ( `id` int NOT NULL AUTO_INCREMENT,`time` datetime(1) DEFAULT NULL,"
    sql2=mojiretsu
    sql3=",PRIMARY KEY (`id`))" 
    sql_all=sql+sql2+sql3
    dbname='trig600vib_'+todaydetail_str
    cur.execute(sql_all % dbname)
    conn.commit()
    cur.close()
except:
    print(sys.exc_info())
finally:
    conn.close()

try:
    # コネクションの作成
    conn = mydb.connect(
        host='127.0.0.1',
        port='3306',
        user='test',
        password='tkroyc123',
        database='mat_db'
    )
    cur = conn.cursor()
    sql ="CREATE TABLE %s (\
      `id` int NOT NULL AUTO_INCREMENT,\
      `time` datetime(1) NOT NULL,\
      `sync1` float,\
      `sync2` float,\
      `meand1low` float,\
      `meand1hi` float,\
      `meand2low` float,\
      `meand2hi` float,\
      `meand3low` float,\
      `meand3hi` float,\
      `rotat1low` float,\
      `rotat1hi` float,\
      `rotat2low` float,\
      `rotat2hi` float,\
      `rotat3low` float,\
      `rotat3hi` float,\
      `flow1low` float,\
      `flow1hi` float,\
      `synclow` float,\
      `sampletime` float,\
      `rms` float,\
      `OA` float,\
      PRIMARY KEY (`id`))"
    tablename600='trig600set_'+todaydetail_str
    cur.execute(sql % tablename600)
    conn.commit()
    cur.close()
except:
    print(sys.exc_info())
finally:
    conn.close()
p_time=time.time()-start
print(p_time)
def func1(x,y):       
    h=22+x*4
    plc16_val1=y[h+2]+y[h+3]+y[h]+y[h+1]
    plc16_val2=y[h+6]+y[h+7]+y[h+4]+y[h+5]
    plc32_val=plc16_val2+plc16_val1
    b=int(plc32_val,16) #16進数文字列を数値に変換
    plc10_num1=s32(b) #10進数符号付きに変換
    return plc10_num1

def func2(x,y):       
    h=22+x*4
    plc16_val1=y[h+2]+y[h+3]+y[h]+y[h+1]
    b=int(plc16_val1,16) #16進数文字列を数値に変換
    plc10_num1=s16(b) #10進数符号付きに変換
    return plc10_num1

def func3():
    global  tablename05
    todaydetail = datetime.datetime.today()
    todaydetail_str=todaydetail.strftime('%Y%m%d')
    #
    if tablename05!='trig05_'+todaydetail_str:
        #データベース生成
        try:
            # コネクションの作成
            conn = mydb.connect(
                host='127.0.0.1',
                port='3306',
                user='test',
                password='tkroyc123',
                database='mat_db'
            )
            cur = conn.cursor()
            sql ="CREATE TABLE %s (\
            `id` int NOT NULL AUTO_INCREMENT,\
            `time` datetime(1) NOT NULL,\
            `rotate1` float DEFAULT NULL,\
            `rotate2` float DEFAULT NULL,\
            `rotate3` float DEFAULT NULL,\
            PRIMARY KEY (`id`))"

            tablename05='trig05_'+todaydetail_str
            #tablename='trig05_20210905'
            cur.execute(sql % tablename05)
            conn.commit()
            cur.close()
        except:
            print(sys.exc_info())
        finally:
            conn.close()
    #(1)空のcsvファイル生成
    todaydetail = datetime.datetime.today()
    t1=todaydetail.strftime("%Y%m%d%H")
    fname1=t1+'_1'+'.csv'
    fname2=t1+'_2'+'.csv'
    fname3=t1+'_3'+'.csv'#20190710追加
    fname4=t1+'_4'+'.csv'
    file_name=joined_path_1+'/'+fname1
    file_name2=joined_path_2+'/'+fname2
    file_name3=joined_path_3+'/'+fname3#20190710追加
    file_name4=joined_path_4+'/'+fname4
    with open(file_name,mode,newline='')as file_obj:
            csv_writer=csv.writer(file_obj)
    with open(file_name2,mode,newline='')as file_obj:
            csv_writer=csv.writer(file_obj)
    with open(file_name3,mode,newline='')as file_obj:#20190710追加
            csv_writer=csv.writer(file_obj)
    with open(file_name4,mode,newline='')as file_obj:
            csv_writer=csv.writer(file_obj)
        
    #(2)フォルダの中身を確認
    #    ファイル名!＝現在時刻のファイルがあるときリネイムする
    files1 = os.listdir(joined_path_1)
    files2 = os.listdir(joined_path_2)
    files3 = os.listdir(joined_path_3)#20190710追加
    files4 = os.listdir(joined_path_4)
    #files_all=[files1,files2,files3,files4]
    for file in files1:
            dtime=file[0:4]+'/'+file[4:6]+'/'+file[6:8]+' '+file[8:10]#12018/4/27 15のような表記
            com_dtime=datetime.datetime.strptime(dtime, '%Y/%m/%d %H')#文字列を日付に変更
            todaydetail = datetime.datetime.today()
            t2=todaydetail.strftime("%Y/%m/%d %H")
            com_t2=datetime.datetime.strptime(t2, '%Y/%m/%d %H')
        #    com_t3=com_t2 - datetime.timedelta(minutes=1)#日付の加算・減算を行うには、datetime.timedeltaを使用する。
            if com_dtime!=com_t2:
                os.renames(joined_path_1+'/'+file,joined_path2_1+'/'+file[:8]+'/'+file)

    for file2 in files2:
            dtime=file2[0:4]+'/'+file2[4:6]+'/'+file2[6:8]+' '+file2[8:10]#12018/4/27 15のような表記
            com_dtime=datetime.datetime.strptime(dtime, '%Y/%m/%d %H')#文字列を日付に変更
            todaydetail = datetime.datetime.today()
            t2=todaydetail.strftime("%Y/%m/%d %H")
            com_t2=datetime.datetime.strptime(t2, '%Y/%m/%d %H')
        #    com_t3=com_t2 - datetime.timedelta(minutes=1)#日付の加算・減算を行うには、datetime.timedeltaを使用する。
            if com_dtime!=com_t2:
                os.renames(joined_path_2+'/'+file2,joined_path2_2+'/'+file2[:8]+'/'+file2)
 
    for file3 in files3:#20190710追加
            dtime=file3[0:4]+'/'+file3[4:6]+'/'+file3[6:8]+' '+file3[8:10]#12018/4/27 15のような表記
            com_dtime=datetime.datetime.strptime(dtime, '%Y/%m/%d %H')#文字列を日付に変更
            todaydetail = datetime.datetime.today()
            t2=todaydetail.strftime("%Y/%m/%d %H")
            com_t2=datetime.datetime.strptime(t2, '%Y/%m/%d %H')
        #    com_t3=com_t2 - datetime.timedelta(minutes=1)#日付の加算・減算を行うには、datetime.timedeltaを使用する。
            if com_dtime!=com_t2:
                os.renames(joined_path_3+'/'+file3,joined_path2_3+'/'+file3[:8]+'/'+file3)
  
    for file4 in files4:#20190710追加
            dtime=file4[0:4]+'/'+file4[4:6]+'/'+file4[6:8]+' '+file4[8:10]#12018/4/27 15のような表記
            com_dtime=datetime.datetime.strptime(dtime, '%Y/%m/%d %H')#文字列を日付に変更
            todaydetail = datetime.datetime.today()
            t2=todaydetail.strftime("%Y/%m/%d %H")
            com_t2=datetime.datetime.strptime(t2, '%Y/%m/%d %H')
        #    com_t3=com_t2 - datetime.timedelta(minutes=1)#日付の加算・減算を行うには、datetime.timedeltaを使用する。
            if com_dtime!=com_t2:
                os.renames(joined_path_4+'/'+file4,joined_path2_4+'/'+file4[:8]+'/'+file4)


    #(3)   ファイルサイズが０の場合タイトルをつける
    filesize=os.path.getsize(file_name)        
    if filesize==0:
        box1=['時間','蛇行量１','蛇行量２','蛇行量３','流量１','流量２','流量３']                      
        with open(file_name,mode,newline='')as file_obj:
            csv_writer=csv.writer(file_obj)
            csv_writer.writerow(box1)

    filesize2=os.path.getsize(file_name2)        
    if filesize2==0:
        box2=['時間']              
        box2.extend(strage)
        with open(file_name2,mode,newline='')as file_obj:
            csv_writer=csv.writer(file_obj)
            csv_writer.writerow(box2)
    
    filesize3=os.path.getsize(file_name3)#20190710追加    
    if filesize3==0:
        box3=['時間','コンパ同期率1','コンパ同期率2','フォーミング下','フォーミング上','バインダ下','バインダ上',
                'オーブン下','バインダ上','コンパ1下','コンパ1上','コンパ2下','コンパ2上','サーフェース下','サーフェース上',
                '流量下','流量上','コンパ同期下限','サンプリング時間','振動rms','振動OA']  #20190726追記            
        with open(file_name3,mode,newline='')as file_obj:
            csv_writer=csv.writer(file_obj)
            csv_writer.writerow(box3)
    
    filesize=os.path.getsize(file_name4)        
    if filesize==0:
        box4=['時間','回転１','回転２','回転３']                      
        with open(file_name4,mode,newline='')as file_obj:
            csv_writer=csv.writer(file_obj)
            csv_writer.writerow(box4) 

    return file_name,file_name2,file_name3,file_name4,todaydetail

def func_05():
    global tablename
    start=time.time()
    file_name,file_name2,file_name3,file_name4,todaydetail=func3()

    time1=todaydetail.strftime('%Y-%m-%d %H:%M:%S.%f')

    #(5)PLCと通信
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #オブジェクトの作成をします
        client.connect((host, port)) #これでサーバーに接続します
        plc_ret1_0=client.send(byte_data1) #適当なデータを送信します（届く側にわかるように）
        plc_ret1_0=client.recv(4096) #レシーブは適当な2の累乗にします（大きすぎるとダメ）
        plc_ret1=plc_ret1_0.hex()
        client.close()
    except:
        print('通信エラー')
        print(time1)
        print(sys.exc_info())
        time.sleep(2)
        client.close()

    #(6)PLCの値をCSVに入れる
    box_2[0]=todaydetail   
    box_2[1]=v4=func1(30,plc_ret1)/100000
    box_2[2]=v5=func1(40,plc_ret1)/100000
    box_2[3]=v6=func1(50,plc_ret1)/100000
    with open(file_name4,mode,newline='')as file_obj:
        csv_writer=csv.writer(file_obj)
        csv_writer.writerow(box_2)
    #220111
    try:
        # データベース接続とカーソル生成
        conn = mydb.connect(
            host='127.0.0.1',
            port='3306',
            user='test',
            password='tkroyc123',
            database='mat_db'
        )        
        cur = conn.cursor()
        tablename05='trig05_'+todaydetail_str
        sql_1 = 'insert into '+tablename05
        sql_2 = '(time,rotate1,rotate2,rotate3) values (%s,%s,%s,%s)'
        sql_3 = sql_1+sql_2       
        data = (todaydetail,box_2[1],box_2[2],box_2[3])
        cur.execute(sql_3,data)
        conn.commit()
        cur.close()
    except:
        print(sys.exc_info())
    finally:
        conn.close()
    p_time=time.time()-start
    #print(p_time)

def func_10():
    global tablename
    start=time.time()
    file_name,file_name2,file_name3,file_name4,todaydetail=func3()

    time1=todaydetail.strftime('%Y-%m-%d %H:%M:%S.%f')

    #(5)PLCと通信
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #オブジェクトの作成をします
        client.connect((host, port)) #これでサーバーに接続します
        plc_ret1_0=client.send(byte_data1) #適当なデータを送信します（届く側にわかるように）
        plc_ret1_0=client.recv(4096) #レシーブは適当な2の累乗にします（大きすぎるとダメ）
        plc_ret1=plc_ret1_0.hex()
        client.close()
    except:
        print('通信エラー')
        print(time1)
        print(sys.exc_info())
        time.sleep(2)
        client.close()

    #(6)PLCの値をCSVに入れる
    box_2[0]=todaydetail   
    box_2[1]=v4=func1(30,plc_ret1)/100000
    box_2[2]=v5=func1(40,plc_ret1)/100000
    box_2[3]=v6=func1(50,plc_ret1)/100000
    with open(file_name4,mode,newline='')as file_obj:
        csv_writer=csv.writer(file_obj)
        csv_writer.writerow(box_2)
        
    box[0]=todaydetail   
    box[1]=v1=func1(0,plc_ret1)
    box[2]=v2=func1(10,plc_ret1)
    box[3]=v3=func1(20,plc_ret1)
    box[4]=v7=func1(60,plc_ret1)/100
    box[5]=v8=func1(70,plc_ret1)/100
    box[6]=v9=func1(80,plc_ret1)/100
    with open(file_name,mode,newline='')as file_obj:
        csv_writer=csv.writer(file_obj)
        csv_writer.writerow(box)
    
    try:
        # データベース接続とカーソル生成
        conn = mydb.connect(
            host='127.0.0.1',
            port='3306',
            user='test',
            password='tkroyc123',
            database='mat_db'
        )
        
        cur = conn.cursor()
        tablename05='trig05_'+todaydetail_str
        sql_1 = 'insert into '+tablename05
        sql_2 = '(time,rotate1,rotate2,rotate3) values (%s,%s,%s,%s)'
        sql_3 = sql_1+sql_2
        data = (todaydetail,box_2[1],box_2[2],box_2[3])
        cur.execute(sql_3,data)
        conn.commit()
        cur.close()
    except:
        print(sys.exc_info())
    finally:
        conn.close()
    try:
        # データベース接続とカーソル生成
        conn = mydb.connect(
            host='127.0.0.1',
            port='3306',
            user='test',
            password='tkroyc123',
            database='mat_db'
        )
        cur = conn.cursor()
        tablename10='trig10_'+todaydetail_str
        sql_1 = 'insert into '+tablename10
        sql_2 = '(time,meand1,meand2,meand3,flow1) values (%s,%s,%s,%s,%s)'
        sql_3 = sql_1+sql_2
        data = (todaydetail,box[1],box[2],box[3],box[4])
        cur.execute(sql_3,data)
        conn.commit()
        cur.close()
    except:
        print(sys.exc_info())
    finally:
        conn.close()
    p_time=time.time()-start
    #print(p_time)
    #time.sleep(0.5)

def func_600():
    global tablename
    start=time.time()
    file_name,file_name2,file_name3,file_name4,todaydetail=func3()

    time1=todaydetail.strftime('%Y-%m-%d %H:%M:%S.%f')

    #(5)PLCと通信
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #オブジェクトの作成をします
        client.connect((host, port)) #これでサーバーに接続します
        plc_ret1_0=client.send(byte_data1) #適当なデータを送信します（届く側にわかるように）
        plc_ret1_0=client.recv(4096) #レシーブは適当な2の累乗にします（大きすぎるとダメ）
        plc_ret1=plc_ret1_0.hex()

        plc_ret2_0=client.send(byte_data2) #適当なデータを送信します（届く側にわかるように）
        plc_ret2_0=client.recv(4096) #レシーブは適当な2の累乗にします（大きすぎるとダメ）
        plc_ret2=plc_ret2_0.hex()
        plc_ret2_2=client.send(byte_data2_2) #適当なデータを送信します（届く側にわかるように）
        plc_ret2_2=client.recv(4096) #レシーブは適当な2の累乗にします（大きすぎるとダメ）
        plc_ret22=plc_ret2_2.hex()
        plc_ret2_3=client.send(byte_data2_3) #適当なデータを送信します（届く側にわかるように）
        plc_ret2_3=client.recv(4096) #レシーブは適当な2の累乗にします（大きすぎるとダメ）
        plc_ret23=plc_ret2_3.hex()
        plc_ret2_4=client.send(byte_data2_4) #適当なデータを送信します（届く側にわかるように）
        plc_ret2_4=client.recv(4096) #レシーブは適当な2の累乗にします（大きすぎるとダメ）
        plc_ret24=plc_ret2_4.hex()
        plc_ret2_5=client.send(byte_data2_5) #適当なデータを送信します（届く側にわかるように）
        plc_ret2_5=client.recv(4096) #レシーブは適当な2の累乗にします（大きすぎるとダメ）
        plc_ret25=plc_ret2_5.hex()
        client.close()
    except:
        print('通信エラー')
        print(time1)
        print(sys.exc_info())
        time.sleep(2)
        client.close()
        

    #(6)PLCの値をCSVに入れる
    box_2[0]=todaydetail   
    box_2[1]=v4=func1(30,plc_ret1)/100000
    box_2[2]=v5=func1(40,plc_ret1)/100000
    box_2[3]=v6=func1(50,plc_ret1)/100000
    with open(file_name4,mode,newline='')as file_obj:
        csv_writer=csv.writer(file_obj)
        csv_writer.writerow(box_2)
        
    box[0]=todaydetail   
    box[1]=v1=func1(0,plc_ret1)
    box[2]=v2=func1(10,plc_ret1)
    box[3]=v3=func1(20,plc_ret1)
    box[4]=v7=func1(60,plc_ret1)/100
    box[5]=v8=func1(70,plc_ret1)/100
    box[6]=v9=func1(80,plc_ret1)/100
    with open(file_name,mode,newline='')as file_obj:
        csv_writer=csv.writer(file_obj)
        csv_writer.writerow(box)

    box_1[0]=todaydetail
    box_1[1]=w1=func1(90,plc_ret1)      
    box_1[2]=w2=func1(92,plc_ret1)
    box_1[3]=w3=func1(100,plc_ret1)
    box_1[4]=w4=func1(102,plc_ret1)
    box_1[5]=w5=func1(110,plc_ret1)
    box_1[6]=w6=func1(112,plc_ret1)
    box_1[7]=w7=func1(120,plc_ret1)
    box_1[8]=w8=func1(122,plc_ret1)
    box_1[9]=w9=func1(130,plc_ret1)/100000
    box_1[10]=w10=func1(132,plc_ret1)/100000
    box_1[11]=w11=func1(140,plc_ret1)/100000
    box_1[12]=w12=func1(142,plc_ret1)/100000
    box_1[13]=w13=func1(150,plc_ret1)/100000
    box_1[14]=w14=func1(152,plc_ret1)/100000
    box_1[15]=w15=func1(160,plc_ret1)/100
    box_1[16]=w16=func1(162,plc_ret1)/100
    box_1[17]=w17=func1(190,plc_ret1)
    box_1[18]=w18=func1(200,plc_ret1)#20190726追記
    box_1[19]=w19=func1(210,plc_ret1)/100#20190726追記
    box_1[20]=w20=func1(220,plc_ret1)#20190726追記
    strage3=[]
    print(len(plc_ret2))#220107test
    try:
        for i in range(0,200):
            v=func2(i,plc_ret2)
            strage3.append(v)
        for i in range(0,200):
            v=func2(i,plc_ret22)
            strage3.append(v)
        for i in range(0,200):
            v=func2(i,plc_ret23)
            strage3.append(v)
        for i in range(0,200):
            v=func2(i,plc_ret24)
            strage3.append(v)
    except:
        print(plc_ret2)
        print(todaydetail)
        print(i)
        print(sys.exc_info())
        time.sleep(1)
        
    datalist=[todaydetail]
    datalist.extend(strage3)

    with open(file_name2,mode,newline='')as file_obj:
        csv_writer=csv.writer(file_obj)
        csv_writer.writerow(datalist)
    with open(file_name3,mode,newline='')as file_obj:
        csv_writer=csv.writer(file_obj)
        csv_writer.writerow(box_1)

    try:
        # データベース接続とカーソル生成
        conn = mydb.connect(
            host='127.0.0.1',
            port='3306',
            user='test',
            password='tkroyc123',
            database='mat_db'
        )
        
        cur = conn.cursor()
        tablename05='trig05_'+todaydetail_str
        sql_1 = 'insert into '+tablename05
        sql_2 = '(time,rotate1,rotate2,rotate3) values (%s,%s,%s,%s)'
        sql_3 = sql_1+sql_2
        data = (todaydetail,box_2[1],box_2[2],box_2[3])
        cur.execute(sql_3,data)
        conn.commit()
        cur.close()
    except:
        print(sys.exc_info())
    finally:
        conn.close()
    try:
        # データベース接続とカーソル生成
        conn = mydb.connect(
            host='127.0.0.1',
            port='3306',
            user='test',
            password='tkroyc123',
            database='mat_db'
        )
        cur = conn.cursor()
        tablename10='trig10_'+todaydetail_str
        sql_1 = 'insert into '+tablename10
        sql_2 = '(time,meand1,meand2,meand3,flow1) values (%s,%s,%s,%s,%s)'
        sql_3 = sql_1+sql_2
        data = (todaydetail,box[1],box[2],box[3],box[4])
        cur.execute(sql_3,data)
        conn.commit()
        cur.close()
    except:
        print(sys.exc_info())
    finally:
        conn.close()

    try:
        # データベース接続とカーソル生成
        conn = mydb.connect(
            host='127.0.0.1',
            port='3306',
            user='test',
            password='tkroyc123',
            database='mat_db'
        )
        cur = conn.cursor()
        tablename600='trig600set_'+todaydetail_str
        sql_1 = 'insert into '+tablename600
        sql_2 = '(time,sync1,sync2,meand1low,meand1hi,\
            meand2low,meand2hi,meand3low,meand3hi,rotat1low,rotat1hi,rotat2low,rotat2hi,\
                rotat3low,rotat3hi,flow1low,flow1hi,synclow,sampletime,rms,OA)\
                     values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,\
                        %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,\
                            %s)'
        sql_3 = sql_1+sql_2
        data = (todaydetail,box_1[1],box_1[2],box_1[3],box_1[4],box_1[5],box_1[6],box_1[7],\
            box_1[8],box_1[9],box_1[10],box_1[11],box_1[12],box_1[13],box_1[14],\
                box_1[15],box_1[16],box_1[17],box_1[18],box_1[19],box_1[20])
        cur.execute(sql_3,data)
        conn.commit()
        cur.close()
    except:
        print(sys.exc_info())
    finally:
        conn.close()
    
    try:
        # データベース接続とカーソル生成
        conn = mydb.connect(
            host='127.0.0.1',
            port='3306',
            user='test',
            password='tkroyc123',
            database='mat_db'
        )
        cur = conn.cursor()
        tablename600='trig600vib_'+todaydetail_str
        sql_1 = 'insert into '+tablename600
        sql_2 = '(time,'+mojiretsu3+') '+'values('+mojiretsu2+')'
        sql_3 = sql_1+sql_2
        data  = tuple(datalist)
        cur.execute(sql_3,data)
        conn.commit()
        cur.close()
    except:
        print(sys.exc_info())
    finally:
        conn.close()
    p_time=time.time()-start
    #print(p_time)

if __name__ == '__main__':
    func_600()









# %%



# %%
