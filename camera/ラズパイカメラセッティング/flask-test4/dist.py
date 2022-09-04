# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 23:02:47 2021

@author: 18530
"""

# dist.py
# /distを静的フォルダとして定義する
from flask import Blueprint
app = Blueprint("dist", __name__,
    static_url_path='/video', static_folder='./video'
)

