#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#%%
import shutil
import os
import pandas as pd
from natsort import natsorted

fname1='./save/1'
fname2='./save/2'
fname3='./save/3'
fname4='./save/4'

fnamelist1=natsorted(os.listdir(fname1))
fnamelist2=natsorted(os.listdir(fname2))
fnamelist3=natsorted(os.listdir(fname3))
fnamelist4=natsorted(os.listdir(fname4))

if len(fnamelist1)>=100:
    print('csv消去します')
    for i in range(0,len(fnamelist1)-100):
        shutil.rmtree(fname1+'/'+fnamelist1[i])
    for i in range(0,len(fnamelist2)-100):
        shutil.rmtree(fname2+'/'+fnamelist2[i])
    for i in range(0,len(fnamelist3)-100):
        shutil.rmtree(fname3+'/'+fnamelist3[i])
    for i in range(0,len(fnamelist4)-100):
        shutil.rmtree(fname4+'/'+fnamelist4[i])
    
else:
    print(len(fnamelist1))

# %%
