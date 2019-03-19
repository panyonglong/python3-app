from .database import db
from .base import Base
print('admin')

class Admin(Base, db.Model):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(120))

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<Admin %s>' % (self.name)

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
            'mysql_comment': '后台表'
        }
    )
