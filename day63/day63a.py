from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import  Column,Integer,String,ForeignKey,UniqueConstraint,Index,VARCHAR,CHAR


# 创建表
Base=declarative_base()
class UserType(Base):
    __tablename__='usertype'
    id=Column(Integer,primary_key=True,autoincrement=True)
    title=Column(VARCHAR(32))

class Users(Base):
    __tablename__='users'
    id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(VARCHAR(32),nullable=True)
    email=Column(String(32),unique=True)
    user_type_id=Column(Integer,ForeignKey('usertype.id'))

    __table_args__=(
       UniqueConstraint('id','name',name='mix_id_name'),
        Index('ix_n_ex','name','email',)
    )

#engine=create_engine('mysql+pymysql://root:degnity0304@127.0.0.1:3306/db7?charset=utf8',max_overflow=5)
# Base.metadata.create_all(engine)
# Base.metadata.drop_all(engine)


# 增
'''
类  表
对象---行
'''
# engine=create_engine('mysql+pymysql://root:degnity0304@127.0.0.1:3306/db7?charset=utf8',max_overflow=5)
# Session=sessionmaker(bind=engine)
# session=Session()
#插入一条
# obj1=UserType(title='普通用户')
# session.add(obj1)
#插入多条
# obj2=[
# UserType(title='黑铁用户'),
# UserType(title='白银用户'),
# UserType(title='黄金用户'),
# UserType(title='黑金用户')
# ]
# session.add_all(obj2)
# session.commit()
# session.close()

#查  类就代表表
engine=create_engine('mysql+pymysql://root:degnity0304@127.0.0.1:3306/db7?charset=utf8',max_overflow=5)
#拿到链接
Session=sessionmaker(bind=engine)
session=Session()
#打印结果可知 直接生成了sql语句
# print(session.query(UserType))
#查询所有
# user_type_list=session.query(UserType).all()
# # 通过打印print(user_type_list)  可以返回的列表内全部是UserType的对象
# print(user_type_list)
# print(type(user_type_list[0]))
# for row in user_type_list:
#     print(row.id,row.title)
# 筛选  query --select **   filter相当与where
# user_type_list=session.query(UserType.id,UserType.title).filter(UserType.id>3)
# for row in user_type_list:
#     print(row.id,row.title)

# sqlalchemy 想要删除操作 必须要先查
# session.query(UserType).filter(UserType.id>3).delete()
# session.commit()



# 更改

session.query(UserType).filter(UserType.id>2).update({"title":"山东大李逵"})
session.commit()

#在原有基础上进行更改
# 列值为字符串类型
session.query(UserType).filter(UserType.id > 2).update({UserType.title: UserType.title + "099"}, synchronize_session=False)

#列值为数字类型
session.query(UserType).filter(UserType.id > 2).update({"num": UserType.num + 1}, synchronize_session="evaluate")