#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#%%
import datetime
import csv
import time

# 日時の取得
now = datetime.datetime.now()
# ディレクトリの指定はここ
filename = './csvtest/log.csv'

# ファイル，1行目(カラム)の作成
with open(filename, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['time','x','y','z'])

x,y,z = 0,0,0
while True:
    # なんらかの処理を書く
    x += 1
    y += 2
    z += 3
    now_str = datetime.datetime.now().strftime('%H:%M:%S')

    # filenameを作成したファイル名に合わせる
    # writer.writerowでlistをcsvに書き込む
    with open(filename, 'a', newline="") as f:
        writer = csv.writer(f)
        writer.writerow([now_str, x, y, z])

    time.sleep(1)
# %%
