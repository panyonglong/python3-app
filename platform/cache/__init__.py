import redis as Redis
from common.app import app

print("redis")

REDIS_CONFIG = app.config['REDIS_CONFIG']
pool = Redis.ConnectionPool(**REDIS_CONFIG)
redis = Redis.Redis(connection_pool=pool)

