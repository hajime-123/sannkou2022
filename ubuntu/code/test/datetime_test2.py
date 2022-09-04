# %%
import datetime
import time

import logging
from logging.handlers import TimedRotatingFileHandler
import sys

#--------------------------
#rootロガーを取得
logger = logging.getLogger()#インスタンス化
# ログレベルを DEBUG に変更 デフォルトは値は warning info, debug はコンソールに出力されない
logger.setLevel(logging.DEBUG)#fh.setLevel(logging.DEBUG)に加えて必要
#出力のフォーマットを定義
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
#ファイルへ出力するハンドラーを定義
#when='D','H','M'
fh=logging.handlers.TimedRotatingFileHandler(filename='log/drawlog.txt',
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
t2=todaydetail.strftime("%M%S.%f")
#t2=dt.strftime("%M%S.%f")
trig05=t2[5]
trig10_now=t2[3]
trig10_pas=t2[3]
trig600_now=t2[1]
trig600_pas=t2[1]
while True:
    start=time.time()
    todaydetail = datetime.datetime.today()#210921
    t2=todaydetail.strftime("%M%S.%f")
    trig05=t2[5]
    trig10_now=t2[3]
    trig600_now=t2[1]
    #print(trig10_now)
    
    if trig600_now!=trig600_pas:
        print('60.0秒',t2)
        logger.debug('60.0秒')
        logger.debug(t2)
    elif trig10_now!=trig10_pas:
        print('1.0秒',t2)
        logger.debug('1.0秒')
        logger.debug(t2)
    elif trig05=='5':
        print('0.5秒',t2)
        logger.debug('0.5秒')
        logger.debug(t2)
    todaydetail = datetime.datetime.today()#210921
    t2=todaydetail.strftime("%M%S.%f")
    trig10_pas=t2[3]
    trig600_pas=t2[1]
    
    #print(trig10_pas)
    time.sleep(0.05)


# %%
