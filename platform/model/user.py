from .database import db
from .base import Base

class User(Base, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(120))
    # 参数分别是 类型 约束key 索引key 是否允许使用空值 默认值
    #email = db.Column(db.String(120), unique=True, index=True, nullable=True, default='')

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %s>' % (self.name)

    __table_args__ = (
        # 联合索引约束key
        db.UniqueConstraint('name', 'email', name='key_name_email'),
        # # 联合索引
        db.Index('idx_name_email', 'name','email'),
        {
            # 设置表引擎
            'mysql_engine': 'InnoDb',
            # 设置表字符集
            'mysql_charset': 'utf8',
            # 设置表描述
            'mysql_comment': '用户表'
        }
    )
