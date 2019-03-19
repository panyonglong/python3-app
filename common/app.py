# 生成应用文件，当做基础
import sys
from flask import Flask
app = Flask(__name__, instance_relative_config=True)

# 运行参数-即环境变量
print(sys.argv)
if len(sys.argv) > 1:
    env = sys.argv[1]
else:
    env = 'prod'

# 载入配置
app.config.from_object('config.env_%s' % env)
