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
import matflask_sub
from natsort import natsorted

app = Flask(__name__)#flaskのインスタンス化

#現在データグラフ#    
#---------------------------------
@app.route("/")
def index():
    title="Matmachine"
    return render_template('index.html', title=title)

@app.route('/page1')
def page1():
    return render_template('page1.html')

@app.route('/postpage1', methods=['POST'])
def postpage1():
    text = request.json['t']
    text2 = request.json['t2']
    #text3 = '4'
    text3 = request.json['t3']
    #lower_text = text
    #lower_text2 = text2
    try:
        plot = matflask_sub.get_line_graph(str(text),str(text2),text3)
        script, div = components(plot)
        return_data = {"result":script,
                       "result2":div,
                       "error":'',
                       }
        return jsonify(ResultSet=json.dumps(return_data))
    except:
        return_data = {"result":'',
                       "result2":'',
                       "error":'データがありません',
                       }
        return jsonify(ResultSet=json.dumps(return_data))

@app.route('/page2')
def page2():
    return render_template('page2.html')

@app.route('/postpage2', methods=['POST'])
def postpage2():
    text = request.json['t']
    text2 = request.json['t2']
    text3 = request.json['t3']
    try:
        plot,sync1,sync2,synclow= matflask_sub.get_line_graph2(str(text),str(text2),text3)
        script, div = components(plot)
        return_data = {"result":script,
                       "result2":div,
                       "result3":sync1,"result4":sync2,"result5":synclow,
                       "error":'',
                       }
        return jsonify(ResultSet=json.dumps(return_data))
    except:
        return_data = {"result":'',
                       "result2":'',
                       "result3":'',"result4":'',"result5":'',
                       "error":'データがありません',
                       }
        return jsonify(ResultSet=json.dumps(return_data))

@app.route('/page3')
def page3():
    return render_template('page3.html')

@app.route('/postpage3', methods=['POST'])
def postpage3():
    text = request.json['t']
    text2 = request.json['t2']
    try:
        plot= matflask_sub.get_line_graph3(str(text),text2)
        script, div = components(plot)
        return_data = {"result":script,
                       "result2":div,
                       "error":''
                       }
        return jsonify(ResultSet=json.dumps(return_data))
    except:
        return_data = {"result":'',
                       "result2":'',
                       "error":'データがありません',
                       }
        return jsonify(ResultSet=json.dumps(return_data))

@app.route('/page4')
def page4():
    return render_template('page4.html')

@app.route('/postpage4', methods=['POST'])
def postpage4():
    text = request.json['t']
    try:
        plot = matflask_sub.get_line_graph4(str(text))
        script, div = components(plot)
        return_data = {"result":script,
                       "result2":div,
                       "error":'',
                       }
        return jsonify(ResultSet=json.dumps(return_data))
    except:
        return_data = {"result":'',
                       "result2":'',
                       "error":'データがありません',
                       }
        return jsonify(ResultSet=json.dumps(return_data))

@app.route('/page5')
def page5():
    return render_template('page5.html')

@app.route('/postpage5', methods=['POST'])
def postpage5():
    text = request.json['t']
    try:
        plot = matflask_sub.get_line_graph5(str(text))
        script, div = components(plot)
        return_data = {"result":script,
                       "result2":div,
                       "error":'',
                       }
        return jsonify(ResultSet=json.dumps(return_data))
    except:
        return_data = {"result":'',
                       "result2":'',
                       "error":'データがありません',
                       }
        return jsonify(ResultSet=json.dumps(return_data))

#過去データグラフ#    
#---------------------------------
@app.route("/past_index")
def past_index():
    title="Matmachine"
    return render_template('past_index.html', title=title)    

@app.route("/past_page1")
def past_page1():
    return render_template('past_page1.html')

@app.route('/past_postpage1', methods=['POST'])
def past_postpage1():
    text = request.json['t']
    text2 = request.json['t_2'].zfill(2)
    text3 = request.json['t_3'].zfill(2)
    text4 = request.json['t_4'].zfill(2)
    select2 = request.json['t2']
    date=text+text2+text3
    date2=date+text4+'_1.csv'
    
    text_2 = request.json['u']
    text2_2 = request.json['u_2'].zfill(2)
    text3_2 = request.json['u_3'].zfill(2)
    text4_2 = request.json['u_4'].zfill(2)
    select2_2 = request.json['u2']
    date_2=text_2+text2_2+text3_2
    date2_2=date_2+text4_2+'_1.csv'
    
    v1=request.json['v1']
    v2=request.json['v2']
    #---------
    try:
        plot =matflask_sub.get_line_graph1_1(date,date2,select2,v1,v2)
        script, div = components(plot)
    except:
        return_data = {"result":'',
                       "result2":'',
                       "result3":'',
                       "error":'データがありません'
                       }
        return jsonify(ResultSet=json.dumps(return_data))
    try:
        plot_2 =matflask_sub.get_line_graph1_1(date_2,date2_2,select2_2,v1,v2)
        script_2, div_2 = components(plot_2)
    except:
        return_data = {"result":script,
                       "result2":div,
                       "result3":date2,
                       "error":'',
                       "result4":'',
                       "result5":'',
                       "result6":'',
                       "error2":'データがありません'
                       }
        return jsonify(ResultSet=json.dumps(return_data))
    
    
    return_data={
            "result":script,
            "result2":div,
            "result3":date2,
            "error":'',
            "result4":script_2,
            "result5":div_2,
            "result6":date2_2,
            "error2":''
            }
    return jsonify(ResultSet=json.dumps(return_data))

@app.route("/past_page2")
def past_page2():
    return render_template('past_page2.html')

@app.route('/past_postpage2', methods=['POST'])
def past_postpage2():
    text = request.json['t']
    text2 = request.json['t_2'].zfill(2)
    text3 = request.json['t_3'].zfill(2)
    text4 = request.json['t_4'].zfill(2)
    select2 = request.json['t2']
    date=text+text2+text3
    date2=date+text4+'_4.csv'
    
    text_2 = request.json['u']
    text2_2 = request.json['u_2'].zfill(2)
    text3_2 = request.json['u_3'].zfill(2)
    text4_2 = request.json['u_4'].zfill(2)
    select2_2 = request.json['u2']
    date_2=text_2+text2_2+text3_2
    date2_2=date_2+text4_2+'_4.csv'
    
    v1=request.json['v1']
    v2=request.json['v2']
    try:
        plot =matflask_sub.get_line_graph2_1(date,date2,select2,v1,v2)
        script, div = components(plot)
    except:
        return_data = {"result":'',
                       "result2":'',
                       "result3":'',
                       "error":'データがありません'
                       }
        return jsonify(ResultSet=json.dumps(return_data))
    try:
        plot_2 =matflask_sub.get_line_graph2_1(date_2,date2_2,select2_2,v1,v2)
        script_2, div_2 = components(plot_2)
    except:
        return_data = {"result":script,
                       "result2":div,
                       "result3":date2,
                       "error":'',
                       "result4":'',
                       "result5":'',
                       "result6":'',
                       "error2":'データがありません'
                       }
        return jsonify(ResultSet=json.dumps(return_data))
    
    
    return_data={
            "result":script,
            "result2":div,
            "result3":date2,
            "error":'',
            "result4":script_2,
            "result5":div_2,
            "result6":date2_2,
            "error2":''
            }
    return jsonify(ResultSet=json.dumps(return_data))

@app.route('/past_page3')
def past_page3():
    return render_template('past_page3.html')

@app.route('/past_postpage3', methods=['POST'])
def past_postpage3():
    text = request.json['t']
    text2 = request.json['t_2'].zfill(2)
    text3 = request.json['t_3'].zfill(2)
    text4 = request.json['t_4'].zfill(2)
    date=text+text2+text3
    date2=date+text4+'_1.csv'
    v1=request.json['v1']
    v2=request.json['v2']
    try:
        plot = matflask_sub.get_line_graph3_1(date,date2,v1,v2)
        script, div = components(plot)
        return_data = {
                "result":script,
                "result2":div,
                "result3":date2,
                "error":''
                       }
        return jsonify(ResultSet=json.dumps(return_data))
    except:
        return_data = {"result":'',
                       "result2":'',
                       "result3":'',
                       "error":'データがありません'
                       }
        return jsonify(ResultSet=json.dumps(return_data))

@app.route('/past_page4')
def past_page4():
    return render_template('past_page4.html')

@app.route('/past_postpage4', methods=['POST'])
def past_postpage4():
    text = request.json['t']
    text2 = request.json['t_2'].zfill(2)
    text3 = request.json['t_3'].zfill(2)
    text4 = request.json['t_4'].zfill(2)
    text5 = request.json['t_5'].zfill(2)
    date=text+text2+text3
    date2=date+text4+'_2.csv'
    date3=date+text4+text5
    try:
        plot = matflask_sub.get_line_graph4_1(date,date2,date3)
        script, div = components(plot)
        return_data = {
                "result":script,
                "result2":div,
                "result3":date,
                "error":''
                       }
        return jsonify(ResultSet=json.dumps(return_data))
    except:
        return_data = {"result":'',
                       "result2":'',
                       "result3":'',
                       "error":'データがありません'
                       }
        return jsonify(ResultSet=json.dumps(return_data))

@app.route('/past_page5')
def past_page5():
    return render_template('past_page5.html')

@app.route('/past_postpage5', methods=['POST'])
def past_postpage5():
    text = request.json['t']
    text2 = request.json['t_2'].zfill(2)
    text3 = request.json['t_3'].zfill(2)
    text4 = request.json['t_4'].zfill(2)
    date=text+text2+text3
    date2=date+text4+'_3.csv'
    try:
        plot = matflask_sub.get_line_graph5_1(date,date2)
        script, div = components(plot)
        return_data = {
                "result":script,
                "result2":div,
                "result3":date,
                "error":''
                       }
        return jsonify(ResultSet=json.dumps(return_data))
    except:
        return_data = {"result":'',
                       "result2":'',
                       "result3":'',
                       "error":'データがありません'
                       }
        return jsonify(ResultSet=json.dumps(return_data))

import dist
app.register_blueprint(dist.app)

import glob
import re
@app.route('/file1')
def root():
    #files=glob.glob('save/1/20200101/*')
    files=glob.glob('save/1/*')
    files=natsorted(files)
    html='<html><meta charset="utf-8"><body>'
    html+='<h1>ファイル一覧</h1>'
    for f in files:
        html+='<p><a href="{0}">{0}</a></p>'.format(f)
    html+='</body></html>'
    return html

@app.route('/save/1/<test>/')
def show_file(test):
    files=glob.glob('save/1/'+test+'/*')
    files=natsorted(files)
    html='<html><meta charset="utf-8"><body>'
    html+='<h1>ファイル一覧</h1>'
    for f in files:
        f2=re.split('/', f)
        #f3=f2[2]#20200101\2020010109_1.csv
        #f4=re.split(r'\\', f3)
        #f4=re.split('/', f3)
        #f5=f4[1]
        f5=f2[3]
        html+='<p><a href="{0}">{0}</a></p>'.format(f5)
        #html+='<p>{0}</p>'.format(f5)
    html+='</body></html>'
    return html

@app.route('/file4')
def root4():
    #files=glob.glob('save/1/20200101/*')
    files=glob.glob('save/1/*')
    files=natsorted(files)
    html='<html><meta charset="utf-8"><body>'
    html+='<h1>ファイル一覧</h1>'
    for f in files:
        html+='<p><a href="{0}">{0}</a></p>'.format(f)
    html+='</body></html>'
    return html

@app.route('/save/4/<test>/')
def show_file4(test):
    files=glob.glob('save/4/'+test+'/*')
    files=natsorted(files)
    html='<html><meta charset="utf-8"><body>'
    html+='<h1>ファイル一覧</h1>'
    for f in files:
        f2=re.split('/', f)
        #f3=f2[2]#20200101\2020010109_1.csv
        #f4=re.split(r'\\', f3)
        #f4=re.split('/', f3)
        #f5=f4[1]
        f5=f2[3]
        html+='<p><a href="{0}">{0}</a></p>'.format(f5)
        #html+='<p>{0}</p>'.format(f5)
    html+='</body></html>'
    return html

if __name__=="__main__":
    #app.run(host='172.21.5.90', port=5000,debug=True,threaded=True)
    app.run(host='172.21.5.160', port=8000,debug=True,threaded=True)
# %%
