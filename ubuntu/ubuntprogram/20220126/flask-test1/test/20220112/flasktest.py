#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#%%
from flask import Flask, render_template, request,jsonify
import mysql.connector as mydb
import json

from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import DatetimeTickFormatter
from math import radians
import datetime
import pandas as pd

app = Flask(__name__)#flaskのインスタンス化

def get_data(x):
    # コネクションの作成
    conn = mydb.connect(
        host='127.0.0.1',
        port='3306',
        user='test',
        password='tkroyc123',
        database='test'
    )
    cur = conn.cursor()
    tablename='test'
    sql_1 = 'select time,val from '+tablename
    sql_2 = ' order by id desc limit %s'
    sql_3 = sql_1+sql_2
    data = (int(x),)
    cur.execute(sql_3,data)
    result_g = cur.fetchall()
    cur.close()
    conn.close()
    return result_g

def get_graph(x):
    conn = mydb.connect(
        host='127.0.0.1',
        port='3306',
        user='test',
        password='tkroyc123',
        database='test'
    )
    cur = conn.cursor()
    tablename='test'
    sql_1 = 'select time,val from '+tablename
    sql_2 = ' order by id desc limit %s'
    sql_3 = sql_1+sql_2
    data = (int(x),)
    cur.execute(sql_3,data)
    result_g = cur.fetchall()
    cur.close()
    conn.close()
    
    boxpd = pd.DataFrame(result_g)
    boxpd_x = boxpd[0].sort_index(ascending=False)
    boxpd_y1 = boxpd[1].sort_index(ascending=False)
    print(boxpd)
    p = figure(x_axis_type='datetime')
    # X軸の設定
    x_format = "%Y-%m-%d %H:%M:%S.%f"
    p.xaxis.formatter = DatetimeTickFormatter(
        milliseconds=[x_format],
        seconds=[x_format],
        minutes=[x_format],
        hours=[x_format],
        days=[x_format],
        months=[x_format],
        years=[x_format]
    )
    p.xaxis.major_label_orientation=radians(90)
    p.line(boxpd_x,boxpd_y1)
    return p

@app.route('/')
def index():
    title="welcomsite"
    #return render_template('/index.html')
    return render_template('/index.html', title=title)

@app.route('/test2', methods=['POST'])
def test2():
    if request.method == 'POST':
        result = request.form['number']
        result2 = get_data(str(result))
        return render_template('/test2.html', data=result, data2=result2)

@app.route('/postpage1', methods=['POST'])
def postpage1():
    result = request.json['t']
    result2 = get_data(str(result))
    return_data = {"result":result2}
    #return_data = {"result":1}
    return jsonify(ResultSet=json.dumps(return_data,default=str))

@app.route('/postpage2', methods=['POST'])
def postpage2():
    result = request.json['t']
    plot = get_graph(str(result))
    script, div = components(plot)
    return_data = {"result2":script,
                    "result3":div,
                    }
    return jsonify(ResultSet=json.dumps(return_data))

if __name__=="__main__":
    app.run(host='172.21.5.90', port=5000,debug=True,threaded=True)
# %%
