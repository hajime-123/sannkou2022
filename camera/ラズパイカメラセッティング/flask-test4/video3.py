import cv2
import time
import datetime
import os
import shutil
import logging
from logging.handlers import TimedRotatingFileHandler
import sys

#保存
todaydetail = datetime.datetime.today()
t1=todaydetail.strftime("%Y%m%d%H%M")
if int(t1[-1])<5:
    t2=t1[:-1]+'0'
else:
    t2=t1[:-1]+'5'
videoname=t2+'.m4v'

#(1)workディレクトリがない場合は作る
woek_path='./video/work'
if os.path.exists(woek_path)!=True:
    os.mkdir(woek_path)

#(2)workディレクトリに入っているデータはsaveへ移動最後にworkディレクトリ作成
files1 = os.listdir(woek_path)
for file in files1:
    #os.renames('../video/work/'+file,'../video/save/'+file)
    shutil.move('./video/work/'+file,'./video/save/'+file)
    if os.path.exists(woek_path)!=True:
        os.mkdir(woek_path)

fmt = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
fps = 10.0
size = (640, 360)
writer = cv2.VideoWriter('./video/work/'+videoname, fmt, fps, size)

URL ="http://127.0.0.1:8080/?action=stream"
s_video = cv2.VideoCapture(URL)
err_count=0

#--------------------------
#rootロガーを取得
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
#出力のフォーマットを定義
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
#ファイルへ出力するハンドラーを定義
#when='D','H','M'
fh=logging.handlers.TimedRotatingFileHandler(filename='logs/videolog.txt',
                                             when='H',
                                             backupCount=7)
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
#rootロガーにハンドラーを登録する
logger.addHandler(fh)
logger.debug('ロギング 開始')
#--------------------------
logger.info(t1)

try:
    while True:
        #logging.basicConfig(filename='logs/'+t1+'error.log',level=logging.DEBUG)
        
        #t3 = time.perf_counter() * 1000
        start = time.time()
        try:
            ret, frame = s_video.read()
            frame = cv2.resize(frame, size)
        except:
            logger.info('通信エラー')
            logger.info(t1)
            time.sleep(20)
            err_count=err_count+1
            logger.info(err_count)
            s_video = cv2.VideoCapture(URL)
            if err_count==5:
                logger.info('再起動してください')
                break
            continue            
        
        todaydetail = datetime.datetime.today()
        t=todaydetail.strftime("%Y/%m/%d/ %H:%M:%S")
        cv2.putText(frame,t,(2,26),cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 2)
        
        #cv2.imshow('frame',frame) 
        writer.write(frame)
        
        nametime1=todaydetail.strftime("%Y%m%d%H%M")
        if int(nametime1[-1])<5:
                nametime2=nametime1[:-1]+'0'
        else:
            nametime2=nametime1[:-1]+'5'
        
        if nametime2!=t2:
                #保存
            writer.release()
            shutil.move('./video/work/'+videoname,'./video/save/'+videoname)#20210329変更
            path='./video/save/'
            files = os.listdir(path)
            files2 = sorted(files)
            MAX_CNT = 10
            for i in range(len(files)-MAX_CNT):
                    logger.info('{}は削除します'.format(files2[i]))
                    os.remove('./video/save/'+files2[i])
            
            if os.path.exists(woek_path)!=True:
                os.mkdir(woek_path)
            fmt = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
            fps = 10.0
            size = (640, 360)
            t2=nametime2
            videoname=t2+'.m4v'
            writer = cv2.VideoWriter('./video/work/'+videoname, fmt, fps, size)
        p_time=time.time() - start    
        sleep_secs = 1 / fps - p_time
        #1/1000は微調整用
        if sleep_secs > 0:
            time.sleep(sleep_secs)
            #print(1)
            #waittime=int(sleep_secs*1000)
        else:
            time.sleep(1/1000)
            #waittime=int((1 / fps)*1000)
            #print(p_time)
        if cv2.waitKey(1) & 0xFF == 13:   
            break
except:
    logger.exception(sys.exc_info())
    