#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#%%
from flask import Blueprint
app = Blueprint("dist", __name__,
    static_url_path='/save', static_folder='./save'
)

# %%
