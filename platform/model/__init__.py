# model 模型
from .database import db

# 引入model类, 主要用于初始化数据库
from . import user
from . import admin

print('db create')

# 创建表
db.create_all()

