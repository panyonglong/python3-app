from .database import db

class Base:
    # 定义添加或修改一条数据的方法
    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return 1
        except Exception as e:
            print(e)
            db.session.rollback()
            return 0

    # 定义添加或修改多条数据的方法
    @staticmethod
    def save_all(*args):
        try:
            db.session.add_all(args)
            db.session.commit()
            return 1
        except Exception as e:
            print(e)
            db.session.rollback()
            return 0

    # 自定义删除方法
    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return 1
        except Exception as e:
            print(e)
            db.session.rollback()
            return 0
