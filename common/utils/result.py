# 工具类函数
# 处理接口返回值

class Result:
    
    def __init__(self, result=None, reason=None, data=None):
        self.result = result
        self.reason = reason
        self.data = data

    def __repr__(self):
        return '<Result %s>' % (self.result)

    def toDict(self):
        req = {
            'result': self.result,
            'reason': self.reason,
            'data': self.data
        }
        return req
