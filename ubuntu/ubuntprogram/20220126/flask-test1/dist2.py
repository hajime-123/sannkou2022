#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#%%
from flask import Blueprint
app = Blueprint("dist2", __name__,
    static_url_path='/save2', static_folder='./save2'
)

# %%
