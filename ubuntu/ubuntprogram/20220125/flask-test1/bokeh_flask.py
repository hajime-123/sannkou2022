#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#%%
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import DatetimeTickFormatter
from math import radians
import datetime
import pandas as pd

from flask import Flask, render_template

app = Flask(__name__)

def get_line_graph():

    
    #second Plot
    d1=datetime.datetime(2021,12,17,8,00,1,500000)
    d2=datetime.datetime(2021,12,17,8,00,1,600000)
    d3=datetime.datetime(2021,12,17,8,00,1,700000) 
    d4=datetime.datetime(2021,12,17,8,00,2,800000) 
    d5=datetime.datetime(2021,12,17,8,00,2,900000) 
    xlist=[d1,d2,d3,d4,d5]
    ylist=[1,2,3,4,5]

    # データをプロット
    p = figure(x_axis_type='datetime')
    #p.line(xlist, ylist)

    d = {
        'a':xlist,
        'b':ylist,
    }
    data_b = pd.DataFrame(d)
    
    p.line('a', 'b', source=data_b)
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
    return p

@app.route('/')
def index():
    line = get_line_graph()
    script, div = components(line)
    return render_template('bokeh_flask.html', script=script, div=div)

if __name__ == "__main__":
   #app.run(host='172.21.5.90', port=5000, debug=True,threaded=True)
   #app.run(host='172.21.5.160', port=5000, debug=True,threaded=True)
   app.run(host='172.21.5.160', port=8000, debug=True,threaded=True)
# %%
