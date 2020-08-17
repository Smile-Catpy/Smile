'''
ORM 查询
'''

import sqlalchemy
import sqlalchemy.ext.declarative  # 父类的结构定义
import sqlalchemy.orm  # ORM的所有工具
import sqlalchemy.orm.session  # 数据库操作的核心
import datetime  # ORM组件要使用具体的日期类型
form app import mysql_pwd
# 定义MySQL数据库方言(直接在连接上通过字符串的形式定义了)以及连接地址
# 当前给定的地址里面还有一个MySql-connector
MYSQL_URL = "mysql+mysqlconnector://root:{}@localhost:3306/E6B034E9E1772CE9B1617B2616B3E507".format(mysql_pwd)


class TEXT(sqlalchemy.ext.declarative.declarative_base()):  # ORM的项目里，每一个映射类都代表一张表
    __tablename__ = "F54B0E0D24F33E50879796722009B500"  # 数据表名称
    id = sqlalchemy.Column(sqlalchemy.BIGINT, primary_key=True)  # 属性域字段映射
    name = sqlalchemy.Column(sqlalchemy.CHAR)
    text = sqlalchemy.Column(sqlalchemy.CHAR)
    timestamp = sqlalchemy.Column(sqlalchemy.TIMESTAMP)

    def __repr__(self) -> str:  # 查询操作
        return "{}:::{}:::{}\n".format(self.name, self.text, self.timestamp)


engine = sqlalchemy.create_engine(MYSQL_URL, encoding="UTF8")  # 返回所有操作信息
sqlalchemy.orm.session.Session = sqlalchemy.orm.sessionmaker(bind=engine)  # 创建session类型
session = sqlalchemy.orm.session.Session()  # 创建session类型（实例对象）


# user = session.query(QQ_9).get(x)  # 查询uid为1 的数据
#    user = session.query(QQ_9).filter(QQ_9.name.like("%小%")).slice(0, 1).all()
# 通过slice进行分页查询，最常用的方法
#    print(user)

def add(name, body):
    time = datetime.datetime.strptime(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
    text = TEXT(name=name, text=body, timestamp=time)
    session.merge(text)
    session.commit()
    session.close()


def delte(id):
    text = session.query(TEXT).get(id)
    session.delete(text)
    session.commit()
    session.close()


def update(id, name, body, time):
    text = session.query(TEXT).get(id)
    session.delete(text)
    newtext = TEXT(id=id, name=name, text=body, timestamp=time)
    session.merge(newtext)
    session.commit()
    session.close()


def check(num=15):
    count = session.query(sqlalchemy.func.count(TEXT.id)).one()
    if num > count[0]:
        text = session.query(TEXT).filter(TEXT.id > 0).all()[::-1]
        return text
    text = session.query(TEXT).filter(TEXT.id >= count[0]-num).all()[::-1]
    # text = str(text[0]).split('\n')
    session.close()
    return text

