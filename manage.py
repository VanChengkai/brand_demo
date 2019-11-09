'''
@Author: your name
@Date: 2019-11-09 19:10:04
@LastEditTime: 2019-11-09 19:20:23
@LastEditors: your name
@Description: In User Settings Edit
@FilePath: \project_2c:\Users\HCK\Desktop\brand promoting\brand_demo\manage.py
'''
from application import app
from flask_script import Manager

manager = Manager(app)

if __name__ == "__main__":
    manager.run()