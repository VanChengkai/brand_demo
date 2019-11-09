'''
@Author: your name
@Date: 2019-11-09 19:15:23
@LastEditTime: 2019-11-09 19:17:43
@LastEditors: your name
@Description: In User Settings Edit
@FilePath: \project_2c:\Users\HCK\Desktop\brand promoting\brand_demo\application\__init__.py
'''
# -*- encoding=UTF-8 —*—
from flask import Flask


app = Flask(__name__)
app.config.from_pyfile('app.conf')
