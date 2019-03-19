# test 环境配置

# 序列化对象成 ascii 编码的 JSON
JSON_AS_ASCII = False

# mysq数据库的url
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/platform?charset=utf8mb4'
# 数据的追踪 当数据发生改变时 会返回信号量 进行关闭 
SQLALCHEMY_TRACK_MODIFICATIONS = False
# 数据库连接池的大小。默认是引擎默认值
SQLALCHEMY_POOL_SIZE = 5
# 设定连接池的连接超时时间。默认是 10 
SQLALCHEMY_POOL_TIMEOUT = 10

REDIS_CONFIG = {
    'host': 'localhost',
    'port': 6379,
    'password': '123456'
}

print("testttttttttttttttt")