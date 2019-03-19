# views 路由视图处理
from common.app import app
from flask import Response, jsonify


# 处理视图函数的返回值
class MyResponse(Response):
    @classmethod
    def force_type(cls, response, environ=None):
        # 列表和字典 转为字符串
        if isinstance(response, (list, dict)):
            response = jsonify(response)
        return super(Response, cls).force_type(response, environ)

app.response_class = MyResponse

# 导入视图函数模块
from .admin import admin
from .user import user

# 注册视图蓝图
app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(user, url_prefix='/user')

