# %%
#----------------
import csv
import datetime
import os
import datetime
import time
#import mat_log05
#import mat_log10
import mat_colltestsub

import logging
from logging.handlers import TimedRotatingFileHandler
import sys


flag=True
mode='a'
b_break=None #終了判定用変数
err_count=0#210115

strage=[]
index=[]
for i in range(1,801):
    v='id'+str(i)
    w=i
    strage.append(v)
    index.append(w)


#--------------------------
#rootロガーを取得
logger = logging.getLogger()#インスタンス化
# ログレベルを DEBUG に変更 デフォルトは値は warning info, debug はコンソールに出力されない
logger.setLevel(logging.DEBUG)#fh.setLevel(logging.DEBUG)に加えて必要
#出力のフォーマットを定義
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
#ファイルへ出力するハンドラーを定義
#when='D','H','M'
fh=logging.handlers.TimedRotatingFileHandler(filename='logs/matlog.txt',
                                             when='H',
                                             backupCount=7)
# ログレベルを DEBUG に変更 デフォルトは値は warning info, debug はコンソールに出力されない
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
#rootロガーにハンドラーを登録する
logger.addHandler(fh)
logger.debug('ロギング 開始')
#--------------------------

todaydetail = datetime.datetime.today()#210921
#dt = datetime.datetime(2018, 2, 1, 12, 5, 30, 2000)
t3=todaydetail.strftime("%M%S.%f")
#t2=dt.strftime("%M%S.%f")
trig05_now=t3[3:6]
trig05_pas=t3[3:6]
trig10_now=t3[3]
trig10_pas=t3[3]
trig600_now=t3[1]
trig600_pas=t3[1]
while True:
    start=time.time()
    todaydetail_3 = datetime.datetime.today()#210921
    t3=todaydetail_3.strftime("%M%S.%f")
    trig05_now=t3[3:6]
    trig10_now=t3[3]
    trig600_now=t3[1]
    #print(trig10_now)
    
    if trig600_now!=trig600_pas:
        print('60.0秒',t3)
        try:
            mat_colltestsub.func_600()
        except:
            logger.exception(sys.exc_info())
            err_count=err_count+1
            if err_count==10:
                print('再起動してください')
                logger.debug('再起動してください')
                break
        logger.debug('60.0秒')
        logger.debug(t3)
    elif trig10_now!=trig10_pas:
        print('1.0秒',t3)
        #mat_log10.func1()
        try:
            mat_colltestsub.func_10()
        except:
            logger.exception(sys.exc_info())
            err_count=err_count+1
            if err_count==10:
                print('再起動してください')
                logger.debug('再起動してください')
                break
        logger.debug('1.0秒')
        logger.debug(t3)
    elif trig05_now!=trig05_pas and trig05_now[2]=='5':
        print('0.5秒',t3)
        try:
            mat_colltestsub.func_05()
        except:
            logger.exception(sys.exc_info())
            err_count=err_count+1
            if err_count==10:
                print('再起動してください')
                logger.debug('再起動してください')
                break
        logger.debug('0.5秒')
        logger.debug(t3)
    todaydetail = datetime.datetime.today()#210921
    t3=todaydetail.strftime("%M%S.%f")
    trig05_pas=t3[3:6]
    trig10_pas=t3[3]
    trig600_pas=t3[1]   
    #print(trig10_pas)
    time.sleep(0.01)

# %%
