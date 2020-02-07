from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import  Column,Integer,String,ForeignKey,UniqueConstraint,Index,VARCHAR,CHAR


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
    user_type_info=relationship('UserType',backref='xxxx')

    __table_args__=(
       UniqueConstraint('id','name',name='mix_id_name'),
        Index('ix_n_ex','name','email',)
    )


engine=create_engine('mysql+pymysql://root:degnity0304@127.0.0.1:3306/db7?charset=utf8',max_overflow=5)
Session=sessionmaker(bind=engine)
session=Session()

# 获取用户信息，以及与其关联的用户类型名称

#没有使用relationship
#此时ret1没有加all 实际上是个生成器
# ret1=session.query(Users,UserType).join(UserType,isouter=True)
# # 在这里 ret 内实际上是列表内嵌套的元组，元组内元素分别是Users和UserType的对象
# print(ret1)
# for a in ret1:
#     print(a[0].id,a[0].name,a[0].user_type_id,a[1].title)

# 使用relationship  实际上relationship 利用外键默认关联了所对应的表
# user_lista=session.query(Users)
# for row in user_lista:
#     print(row.id,row.name,row.user_type_info.title)

#问题2 获取用户类型，以及所有用户
# user_type_info=relationship('UserType',backref='xxxx')
#relationship 中的backref 实际上是传给关联表的操作句柄，以便反向查询
type_list=session.query(UserType).filter(UserType.id<5)
for row in type_list:
    print(row.id,row.title,row.xxxx[0].name,[(a.name,a.id) for a in row.xxxx])

#总之 relationship  提供了正向和反向操作