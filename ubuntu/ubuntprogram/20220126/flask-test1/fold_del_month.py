#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#%%
#----------------

import shutil
import os
import pandas as pd
from natsort import natsorted

fname1='./save2/1'
fname2='./save2/4'


fnamelist1=natsorted(os.listdir(fname1))
fnamelist2=natsorted(os.listdir(fname2))

if len(fnamelist1)>=100:
    #print(fnamelist1[0])
    for i in range(0,len(fnamelist1)-100):
        shutil.rmtree(fname1+'/'+fnamelist1[i])
    for i in range(0,len(fnamelist2)-100):
        shutil.rmtree(fname2+'/'+fnamelist2[i])
    
else:
    print(len(fnamelist1))








# %%



# %%
