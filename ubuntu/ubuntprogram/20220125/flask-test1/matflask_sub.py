#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#%%
import mysql.connector as mydb#220111
import datetime
import pandas as pd
from bokeh.models import DatetimeTickFormatter
from bokeh.plotting import figure
from math import radians
from bokeh.layouts import layout#追加

todaydetail = datetime.datetime.today()
t1=todaydetail.strftime("%Y%m%d%H")
todaydetail_str=todaydetail.strftime('%Y%m%d')#211119

def get_line_graph(x,y,t):
    todaydetail = datetime.datetime.today()
    t1=todaydetail.strftime("%Y%m%d%H")
    todaydetail_str=todaydetail.strftime('%Y%m%d')#211119
    #connection =  sqlite3.connect(db_path,timeout=10000)
    connection = mydb.connect(
            host='127.0.0.1',
            port='3306',
            user='test',
            password='tkroyc123',
            database='mat_db'
        )
    cursor = connection.cursor()
    tablename='trig10_'+todaydetail_str
    sql_1 = 'select time,meand1,meand2,meand3 from '+tablename
    sql_2 = ' order by id desc limit %s'
    sql_3 = sql_1+sql_2
    data = (int(x),)
    cursor.execute(sql_3,data)
    # db_get0 = 'SELECT time,meand1,meand2,meand3 from test1 order by id desc limit '
    # db_get1=x
    # db_get = db_get0+db_get1
    # cursor.execute(db_get)
    result_g = cursor.fetchall()
    cursor.close()
    connection.close() 
    
    boxpd = pd.DataFrame(result_g)
    boxpd_x = pd.to_datetime(boxpd[0])
    boxpd_x = boxpd_x.sort_index(ascending=False)
    if y=='0':
        boxpd_y1 = boxpd[1]
        boxpd_y1 = boxpd_y1.sort_index(ascending=False)
        boxpd_y1_2 = boxpd[2]
        boxpd_y1_2 = boxpd_y1_2.sort_index(ascending=False)
        boxpd_y1_3 = boxpd[3]
        boxpd_y1_3 = boxpd_y1_3.sort_index(ascending=False)
    elif y=='1':
        boxpd_y1 = boxpd[1]
        boxpd_y1 = boxpd_y1.sort_index(ascending=False)
    elif y=='2':
        boxpd_y1_2 = boxpd[2]
        boxpd_y1_2 = boxpd_y1_2.sort_index(ascending=False)
    elif y=='3':
        boxpd_y1_3 = boxpd[3]
        boxpd_y1_3 = boxpd_y1_3.sort_index(ascending=False)
    # create a new plot with a title and axis labels
    fig = figure(title="matmachine meandering", x_axis_type="datetime",
                 tools=['pan','xwheel_zoom','ywheel_zoom','reset','save'])
    #軸の設定
    x_format = "%Y-%m-%d %H:%M:%S.%f"
    fig.xaxis.formatter = DatetimeTickFormatter(
        milliseconds=[x_format],
        seconds=[x_format],
        minutes=[x_format],
        hours=[x_format],
        days=[x_format],
        months=[x_format],
        years=[x_format]
    )
    fig.xaxis.major_label_orientation=radians(90)
    
    connection =  mydb.connect(
            host='127.0.0.1',
            port='3306',
            user='test',
            password='tkroyc123',
            database='mat_db'
        )
    cursor = connection.cursor()
    tablename600='trig600set_'+todaydetail_str
    sql_1 = 'SELECT time,meand1low,meand1hi,meand2low,meand2hi,meand3low,meand3hi from '+tablename600
    sql_2 = ' order by id desc limit %s'
    sql_3 = sql_1+sql_2
    data = (int(1),)
    cursor.execute(sql_3,data)
    # db_get0 = 'SELECT time,meand1low,meand1hi,meand2low,meand2hi,meand3low,meand3hi\
    #  from test3 order by rowid desc limit '
    # db_get1='1'
    # db_get = db_get0+db_get1
    # cursor.execute(db_get)
    result_g = cursor.fetchall()
    cursor.close()
    connection.close() 
    
    boxpd2 = pd.DataFrame(result_g)
    
    testx=boxpd_x.iloc[[0, -1]]
    lowlevel=pd.Series([boxpd2[1][0],boxpd2[1][0]])
    highlevel=pd.Series([boxpd2[2][0],boxpd2[2][0]])
    lowlevel2=pd.Series([boxpd2[3][0],boxpd2[3][0]])
    highlevel2=pd.Series([boxpd2[4][0],boxpd2[4][0]])
    lowlevel3=pd.Series([boxpd2[5][0],boxpd2[5][0]])
    highlevel3=pd.Series([boxpd2[6][0],boxpd2[6][0]])

    # add a line renderer with legend and line thickness
    if y=='0':       
        fig.line(boxpd_x, boxpd_y1,legend='フォーミングネット',line_width=2)
        if t=='5':
            fig.line(testx, lowlevel)
            fig.line(testx, highlevel)
        fig.line(boxpd_x, boxpd_y1_2,color='red',legend='バインダーネット',line_width=2)
        if t=='5':
            fig.line(testx, lowlevel2,color='red')
            fig.line(testx, highlevel2,color='red')
        fig.line(boxpd_x, boxpd_y1_3,color='green',legend='オーブンネット',line_width=2)
        if t=='5':
            fig.line(testx, lowlevel3,color='green')
            fig.line(testx, highlevel3,color='green')
        fig.legend.location='top_left'
        return fig
    elif y=='1':       
        fig.line(boxpd_x, boxpd_y1,legend='フォーミングネット',line_width=2)
        if t=='5':
            fig.line(testx, lowlevel)
            fig.line(testx, highlevel)
        fig.legend.location='top_left'
        return fig
    elif y=='2':       
        fig.line(boxpd_x, boxpd_y1_2,color='red',legend='バインダーネット',line_width=2)
        if t=='5':
            fig.line(testx, lowlevel2,color='red')
            fig.line(testx, highlevel2,color='red')
        fig.legend.location='top_left'
        return fig
    elif y=='3':       
        fig.line(boxpd_x, boxpd_y1_3,color='green',legend='オーブンネット',line_width=2)
        if t=='5':
            fig.line(testx, lowlevel3,color='green')
            fig.line(testx, highlevel3,color='green')
        fig.legend.location='top_left'
        return fig

def get_line_graph2(x,y,t):
    todaydetail = datetime.datetime.today()
    t1=todaydetail.strftime("%Y%m%d%H")
    todaydetail_str=todaydetail.strftime('%Y%m%d')#211119
    connection =  mydb.connect(
            host='127.0.0.1',
            port='3306',
            user='test',
            password='tkroyc123',
            database='mat_db'
        )
    cursor = connection.cursor()
    tablename05='trig05_'+todaydetail_str
    sql_1 = 'SELECT time,rotate1,rotate2,rotate3 from '+tablename05
    sql_2 = ' order by id desc limit %s'
    sql_3 = sql_1+sql_2
    data = (int(x),)
    cursor.execute(sql_3,data)
    # db_get0 = 'SELECT time,rotat1,rotat2,rotat3 from test1 order by rowid desc limit '
    # db_get1=x
    # db_get = db_get0+db_get1
    # cursor.execute(db_get)
    result_g = cursor.fetchall()
    cursor.close()
    connection.close() 
    
    boxpd = pd.DataFrame(result_g)
    boxpd_x = pd.to_datetime(boxpd[0])
    boxpd_x = boxpd_x.sort_index(ascending=False)
    if y=='0':
        boxpd_y1 = boxpd[1]
        boxpd_y1 = boxpd_y1.sort_index(ascending=False)
        boxpd_y1_2 = boxpd[2]
        boxpd_y1_2 = boxpd_y1_2.sort_index(ascending=False)
        boxpd_y1_3 = boxpd[3]
        boxpd_y1_3 = boxpd_y1_3.sort_index(ascending=False) 
    elif y=='1':
        boxpd_y1 = boxpd[1]
        boxpd_y1 = boxpd_y1.sort_index(ascending=False)
    elif y=='2':
        boxpd_y1_2 = boxpd[2]
        boxpd_y1_2 = boxpd_y1_2.sort_index(ascending=False)
    elif y=='3':
        boxpd_y1_3 = boxpd[3]
        boxpd_y1_3 = boxpd_y1_3.sort_index(ascending=False)
    # create a new plot with a title and axis labels
    fig = figure(title="matmachine rotation", x_axis_type="datetime",
                 tools=['pan','xwheel_zoom','ywheel_zoom','reset','save'])
    #軸の設定
    x_format = "%Y-%m-%d %H:%M:%S.%f"
    fig.xaxis.formatter = DatetimeTickFormatter(
        milliseconds=[x_format],
        seconds=[x_format],
        minutes=[x_format],
        hours=[x_format],
        days=[x_format],
        months=[x_format],
        years=[x_format]
    )
    fig.xaxis.major_label_orientation=radians(90)
    
    connection =  mydb.connect(
            host='127.0.0.1',
            port='3306',
            user='test',
            password='tkroyc123',
            database='mat_db'
        )
    cursor = connection.cursor()
    tablename600='trig600set_'+todaydetail_str
    sql_1 = 'select time,rotat1low,rotat1hi,rotat2low,rotat2hi,rotat3low,rotat3hi,sync1,sync2,synclow from '+tablename600
    sql_2 = ' order by id desc limit %s'
    sql_3 = sql_1+sql_2
    data = (int(1),)
    cursor.execute(sql_3,data)
    # db_get0 = 'SELECT time,rotat1low,rotat1hi,rotat2low,rotat2hi,rotat3low,rotat3hi,sync1,sync2,synclow\
    #  from test3 order by rowid desc limit '
    # db_get1='1'
    # db_get = db_get0+db_get1
    # cursor.execute(db_get)
    result_g = cursor.fetchall()
    cursor.close()
    connection.close() 
    
    boxpd2 = pd.DataFrame(result_g)
    
    testx=boxpd_x.iloc[[0, -1]]
    lowlevel=pd.Series([boxpd2[1][0],boxpd2[1][0]])
    highlevel=pd.Series([boxpd2[2][0],boxpd2[2][0]])
    lowlevel2=pd.Series([boxpd2[3][0],boxpd2[3][0]])
    highlevel2=pd.Series([boxpd2[4][0],boxpd2[4][0]])
    lowlevel3=pd.Series([boxpd2[5][0],boxpd2[5][0]])
    highlevel3=pd.Series([boxpd2[6][0],boxpd2[6][0]])
    sync1=str(boxpd2[7][0])
    sync2=str(boxpd2[8][0])
    synclow=str(boxpd2[9][0])
    

    # add a line renderer with legend and line thickness
    if y=='0':
        fig.line(boxpd_x, boxpd_y1,legend='コンパクションローラー1',line_width=2)
        fig.line(boxpd_x, boxpd_y1_2,color='red',legend='コンパクションローラー2',line_width=2)
        fig.line(boxpd_x, boxpd_y1_3,color='green',legend='サーフェースローラー1',line_width=2)
        if t=='5':
            fig.line(testx, lowlevel)
            fig.line(testx, highlevel)
            fig.line(testx, lowlevel2,color='red')
            fig.line(testx, highlevel2,color='red')
            fig.line(testx, lowlevel3,color='green')
            fig.line(testx, highlevel3,color='green')
        fig.legend.location='top_left'
        return fig,sync1,sync2,synclow
    if y=='1':
        fig.line(boxpd_x, boxpd_y1,legend='コンパクションローラー1',line_width=2)
        if t=='5':
            fig.line(testx, lowlevel)
            fig.line(testx, highlevel)
        fig.legend.location='top_left'
        return fig,sync1,sync2,synclow
    if y=='2':
        fig.line(boxpd_x, boxpd_y1_2,color='red',legend='コンパクションローラー2',line_width=2)
        if t=='5':
            fig.line(testx, lowlevel2,color='red')
            fig.line(testx, highlevel2,color='red')
        fig.legend.location='top_left'
        return fig,sync1,sync2,synclow
    if y=='3':
        fig.line(boxpd_x, boxpd_y1_3,color='green',legend='サーフェースローラー',line_width=2)
        if t=='5':
            fig.line(testx, lowlevel3,color='green')
            fig.line(testx, highlevel3,color='green')
        fig.legend.location='top_left'
        return fig,sync1,sync2,synclow

def get_line_graph3(x,t):
    todaydetail = datetime.datetime.today()
    t1=todaydetail.strftime("%Y%m%d%H")
    todaydetail_str=todaydetail.strftime('%Y%m%d')#211119
    connection =  mydb.connect(
            host='127.0.0.1',
            port='3306',
            user='test',
            password='tkroyc123',
            database='mat_db'
        )
    try:
        cursor = connection.cursor()
        tablename10='trig10_'+todaydetail_str
        sql_1 = 'select time,flow1 from '+tablename10
        sql_2 = ' order by id desc limit %s'
        sql_3 = sql_1+sql_2
        data = (int(x),)
        cursor.execute(sql_3,data)
        # db_get0 = 'SELECT time,flow1 from test1 order by rowid desc limit '
        # db_get1=x
        # db_get = db_get0+db_get1
        # cursor.execute(db_get)
        result_g = cursor.fetchall()
    
    finally:
        cursor.close()
        connection.close()
        
    
    boxpd = pd.DataFrame(result_g)
    boxpd_x = pd.to_datetime(boxpd[0])
    boxpd_y1 = boxpd[1]
    boxpd_x = boxpd_x.sort_index(ascending=False)
    boxpd_y1 = boxpd_y1.sort_index(ascending=False)   

    # create a new plot with a title and axis labels
    fig = figure(title="matmachine flow", x_axis_type="datetime",
                 tools=['pan','xwheel_zoom','ywheel_zoom','reset','save'])
    #軸の設定
    format = "%Y-%m-%d-%H-%M-%S"
    fig.xaxis.formatter = DatetimeTickFormatter(
        seconds=[format],
        minsec =[format],
        minutes=[format],
        hourmin=[format],
        hours  =[format],
        days   =[format],
        months =[format],
        years  =[format]
    )
    fig.xaxis.major_label_orientation=radians(90)
    
    connection =  mydb.connect(
            host='127.0.0.1',
            port='3306',
            user='test',
            password='tkroyc123',
            database='mat_db'
        )
    cursor = connection.cursor()
    tablename600='trig600set_'+todaydetail_str
    sql_1 = 'select time,flow1low,flow1hi from '+tablename600
    sql_2 = ' order by id desc limit %s'
    sql_3 = sql_1+sql_2
    data = (int(1),)
    cursor.execute(sql_3,data)
    # db_get0 = 'SELECT time,flow1low,flow1hi\
    #  from test3 order by rowid desc limit '
    # db_get1='1'
    # db_get = db_get0+db_get1
    # cursor.execute(db_get)
    result_g = cursor.fetchall()
    cursor.close()
    connection.close()
    
    boxpd2 = pd.DataFrame(result_g)
    
    testx=boxpd_x.iloc[[0, -1]]
    flow1low=pd.Series([boxpd2[1][0],boxpd2[1][0]])
    flow1hi=pd.Series([boxpd2[2][0],boxpd2[2][0]])

    # add a line renderer with legend and line thickness
    fig.line(boxpd_x, boxpd_y1,legend='流量１',line_width=2)
    if t=='5':
        fig.line(testx, flow1low)
        fig.line(testx, flow1hi)
    fig.legend.location='top_left'
#    print(type(fig))
    return fig

def get_line_graph4(x):
    todaydetail = datetime.datetime.today()
    t1=todaydetail.strftime("%Y%m%d%H")
    todaydetail_str=todaydetail.strftime('%Y%m%d')#211119
    strage=[]
    index=[]
    for i in range(1,801):
        v='id'+str(i)
        w=i
        strage.append(v)
        index.append(w)
    mojiretsu=','.join(strage)
    
    # db_get0 = 'SELECT time1,'+mojiretsu+' from test2 order by rowid desc limit 1 OFFSET '
    # db_get1=x
    # db_get = db_get0+db_get1
    
    connection =  mydb.connect(
            host='127.0.0.1',
            port='3306',
            user='test',
            password='tkroyc123',
            database='mat_db'
        )
    cursor = connection.cursor()
    dbname='trig600vib_'+todaydetail_str
    sql_1 = 'select time,'+mojiretsu+' from '+dbname
    sql_2 = ' order by id desc limit 1 OFFSET %s'
    sql_3 = sql_1+sql_2
    data = (int(x),)
    cursor.execute(sql_3,data)
    #cursor.execute(db_get)
    result_g = cursor.fetchall()
    cursor.close()
    connection.close() 
    
    boxpd = pd.DataFrame(result_g)
    boxpd_time = pd.to_datetime(boxpd[0])
    boxpd_x=pd.DataFrame(index)
    boxpd_y =boxpd.iloc[:,1:801].T
    seri_x = boxpd_x.stack()
    seri_y = boxpd_y.stack()
   
    # create a new plot with a title and axis labels
    fig = figure(title="matmachine frequency"+str(boxpd_time[0]))
    
    # add a line renderer with legend and line thickness
    fig.line(seri_x, seri_y,legend='周波数')
    
    fig.legend.location='top_left'
#    print(type(fig))
    return fig

def get_line_graph5(x):
    todaydetail = datetime.datetime.today()
    t1=todaydetail.strftime("%Y%m%d%H")
    todaydetail_str=todaydetail.strftime('%Y%m%d')#211119
    connection =  mydb.connect(
            host='127.0.0.1',
            port='3306',
            user='test',
            password='tkroyc123',
            database='mat_db'
        )
    try:
        cursor = connection.cursor()
        tablename='trig600set_'+todaydetail_str
        sql_1 = 'select time,OA,rms from '+tablename
        sql_2 = ' order by id desc limit %s'
        sql_3 = sql_1+sql_2
        data = (int(x),)
        cursor.execute(sql_3,data)
        # db_get0 = 'SELECT time,OA,rms from test3 order by rowid desc limit '
        # db_get1=x
        # db_get = db_get0+db_get1
        # cursor.execute(db_get)
        result_g = cursor.fetchall()
    
    finally:
        cursor.close()
        connection.close()
        
    
    boxpd = pd.DataFrame(result_g)
    boxpd_x = pd.to_datetime(boxpd[0])
    boxpd_y1 = boxpd[1]
    boxpd_y2 = boxpd[2]#追加
    boxpd_x = boxpd_x.sort_index(ascending=False)
    boxpd_y1 = boxpd_y1.sort_index(ascending=False)
    boxpd_y2 = boxpd_y2.sort_index(ascending=False)#追加

    # create a new plot with a title and axis labels
    figbox=['fig1','fig2']
    for i in range(2):
        figbox[i] = figure(title="matmachine frequency_transition", x_axis_type="datetime",
                     tools=['pan','xwheel_zoom','ywheel_zoom','reset','save'])
        #軸の設定
        format = "%Y-%m-%d-%H-%M-%S"
        figbox[i].xaxis.formatter = DatetimeTickFormatter(
            seconds=[format],
            minsec =[format],
            minutes=[format],
            hourmin=[format],
            hours  =[format],
            days   =[format],
            months =[format],
            years  =[format]
        )
        figbox[i].xaxis.major_label_orientation=radians(90)
    
    

    # add a line renderer with legend and line thickness
    figbox[0].line(boxpd_x, boxpd_y1,legend='振動OA',line_width=2)
    figbox[0].legend.location='top_left'
    figbox[1].line(boxpd_x, boxpd_y2,legend='振動rms',line_width=2)
    figbox[1].legend.location='top_left'
#    print(type(fig))

    f=layout([[figbox[0]],[figbox[1]]])
    
    return f

def get_line_graph1_1(x,x2,x3,x4,x5):
    file_name='./save/1/'+x+'/'+x2
    boxpd=pd.read_csv(file_name,engine='python',header=0)
    boxpd_x = pd.to_datetime(boxpd['時間'])
    boxpd_y1 = boxpd['蛇行量１']
    boxpd_y1_2 = boxpd['蛇行量２']
    boxpd_y1_3 = boxpd['蛇行量３']
    fig = figure(title="matmachine rotation", x_axis_type="datetime",
                 tools=['pan','xwheel_zoom','ywheel_zoom','reset','save'],
                 y_range=(int(x4),int(x5)))
    #軸の設定
    format = "%Y-%m-%d-%H-%M-%S"
    fig.xaxis.formatter = DatetimeTickFormatter(
        seconds=[format],
        minsec =[format],
        minutes=[format],
        hourmin=[format],
        hours  =[format],
        days   =[format],
        months =[format],
        years  =[format]
    )
    fig.xaxis.major_label_orientation=radians(90)
    
    if x3=='0':       
        fig.line(boxpd_x, boxpd_y1,legend='フォーミングネット蛇行量')
        fig.line(boxpd_x, boxpd_y1_2,color='red',legend='バインダーネット蛇行量')
        fig.line(boxpd_x, boxpd_y1_3,color='green',legend='オーブンネット蛇行量')
        fig.legend.location='top_left'
        return fig
    elif x3=='1':       
        fig.line(boxpd_x, boxpd_y1,legend='フォーミングネット')
        fig.legend.location='top_left'
        return fig
    elif x3=='2':       
        fig.line(boxpd_x, boxpd_y1_2,color='red',legend='バインダーネット')
        fig.legend.location='top_left'
        return fig
    elif x3=='3':       
        fig.line(boxpd_x, boxpd_y1_3,color='green',legend='オーブンネット')
        fig.legend.location='top_left'
        return fig

def get_line_graph2_1(x,x2,x3,x4,x5):
    file_name='./save/4/'+x+'/'+x2
    boxpd=pd.read_csv(file_name,engine='python',header=0)
    boxpd_x = pd.to_datetime(boxpd['時間'])
    boxpd_y1 = boxpd['回転１']
    boxpd_y1_2 = boxpd['回転２']
    boxpd_y1_3 = boxpd['回転３']
    # create a new plot with a title and axis labels
    fig = figure(title="matmachine rotation", x_axis_type="datetime",
                 tools=['pan','xwheel_zoom','ywheel_zoom','reset','save'],
                 y_range=(int(x4),int(x5)))
    #軸の設定
    x_format = "%Y-%m-%d %H:%M:%S.%f"
    fig.xaxis.formatter = DatetimeTickFormatter(
        milliseconds=[x_format],
        seconds=[x_format],
        minutes=[x_format],
        hours=[x_format],
        days=[x_format],
        months=[x_format],
        years=[x_format]
    )
    fig.xaxis.major_label_orientation=radians(90)
    
    # add a line renderer with legend and line thickness
    if x3=='0':       
        fig.line(boxpd_x, boxpd_y1,legend='コンパクションローラー1')
        fig.line(boxpd_x, boxpd_y1_2,color='red',legend='コンパクションローラー2')
        fig.line(boxpd_x, boxpd_y1_3,color='green',legend='サーフェースローラー1')
        fig.legend.location='top_left'
        return fig
    elif x3=='1':       
        fig.line(boxpd_x, boxpd_y1,legend='コンパクションローラー1')
        fig.legend.location='top_left'
        return fig
    elif x3=='2':       
        fig.line(boxpd_x, boxpd_y1_2,color='red',legend='コンパクションローラー2')
        fig.legend.location='top_left'
        return fig
    elif x3=='3':       
        fig.line(boxpd_x, boxpd_y1_3,color='green',legend='サーフェースローラー1')
        fig.legend.location='top_left'
        return fig

def get_line_graph3_1(x,x2,x3,x4):
    file_name='./save/1/'+x+'/'+x2
    boxpd=pd.read_csv(file_name,engine='python',header=0)
    boxpd_x = pd.to_datetime(boxpd['時間'])
    boxpd_y1 = boxpd['流量１']
    # create a new plot with a title and axis labels
    fig = figure(title="matmachine rotation", x_axis_type="datetime",
                 tools=['pan','xwheel_zoom','ywheel_zoom','reset','save'],
                 y_range=(int(x3),int(x4)))
    #軸の設定
    format = "%Y-%m-%d-%H-%M-%S"
    fig.xaxis.formatter = DatetimeTickFormatter(
        seconds=[format],
        minsec =[format],
        minutes=[format],
        hourmin=[format],
        hours  =[format],
        days   =[format],
        months =[format],
        years  =[format]
    )
    fig.xaxis.major_label_orientation=radians(90)
    
    # add a line renderer with legend and line thickness
    fig.line(boxpd_x, boxpd_y1,legend='流量１')
    fig.legend.location='top_left'
#    print(type(fig))
    return fig

def get_line_graph4_1(x,x2,x3):
    strage=[]
    index=[]
    for i in range(1,801):
        v='id'+str(i)
        w=i
        strage.append(v)
        index.append(w)
    file_name='./save/2/'+x+'/'+x2
    boxpd=pd.read_csv(file_name,engine='python',header=0)
    boxpd['時間']= pd.to_datetime(boxpd['時間'])
    boxpd.set_index('時間', inplace=True)
    df=boxpd[x3]
    
    boxpd_x=pd.DataFrame(index)
    boxpd_y=df.T
    seri_x = boxpd_x.stack()
    seri_y = boxpd_y.stack()
   
    # create a new plot with a title and axis labels
    fig = figure(title="matmachine frequency"+str(df.index[0]))
    
    # add a line renderer with legend and line thickness
    fig.line(seri_x, seri_y,legend='周波数')
    
    fig.legend.location='top_left'
#    print(type(fig))
    return fig

def get_line_graph5_1(x,x2):
    file_name='./save/3/'+x+'/'+x2
    boxpd=pd.read_csv(file_name,engine='python',header=0) 
        
    boxpd_x = pd.to_datetime(boxpd['時間'])    
    boxpd_y1 = boxpd['振動rms']
    boxpd_y2 = boxpd['振動OA']
    
    # create a new plot with a title and axis labels
    figbox=['fig1','fig2']
    for i in range(2):
        figbox[i] = figure(title="matmachine frequency_transition", x_axis_type="datetime",
                     tools=['pan','xwheel_zoom','ywheel_zoom','reset','save'])
        #軸の設定
        format = "%Y-%m-%d-%H-%M-%S"
        figbox[i].xaxis.formatter = DatetimeTickFormatter(
            seconds=[format],
            minsec =[format],
            minutes=[format],
            hourmin=[format],
            hours  =[format],
            days   =[format],
            months =[format],
            years  =[format]
        )
        figbox[i].xaxis.major_label_orientation=radians(90)
    
    

    # add a line renderer with legend and line thickness
    figbox[0].line(boxpd_x, boxpd_y1,legend='振動OA',line_width=2)
    figbox[0].legend.location='top_left'
    figbox[1].line(boxpd_x, boxpd_y2,legend='振動rms',line_width=2)
    figbox[1].legend.location='top_left'
#    print(type(fig))

    f=layout([[figbox[0]],[figbox[1]]])
    return f   

import glob
import re
def show_file(test):
    files=glob.glob('save/1/'+test+'/*')
    html='<html><meta charset="utf-8"><body>'
    html+='<h1>ファイル一覧</h1>'
    for f in files:
        f2=re.split('/', f)
        #f3=f2[2]#20200101\2020010109_1.csv
        #20200101\2020010109_1.csv
        #f4=re.split(r'\\', f3)
        #f4=re.split('/', f3)
        #f5=f4[1]
        f5=f2[3]


if __name__=="__main__":
    #get_line_graph2(str(10),str(0),5)
    #get_line_graph3(str(10),5)
    #get_line_graph5(str(10))
    #get_line_graph1_1(str(20220114),'2022011400_1.csv',str(0),str(150),str(300))
    #get_line_graph2_1(str(20220114),'2022011400_4.csv',str(0),str(150),str(300))
    #get_line_graph3_1(str(20220114),'2022011400_4.csv',str(0),str(150),str(300))
    show_file(str(20220114))
# %%
