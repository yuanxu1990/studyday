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

    __table_args__=(
       UniqueConstraint('id','name',name='mix_id_name'),
        Index('ix_n_ex','name','email',)
    )


engine=create_engine('mysql+pymysql://root:degnity0304@127.0.0.1:3306/db7?charset=utf8',max_overflow=5)
Session=sessionmaker(bind=engine)
session=Session()

# obj2=[
# Users(name='李逵',email='3993@qq.com',user_type_id=1),
# Users(name='李逵2',email='39393@qq.com',user_type_id=2),
# Users(name='松江',email='39935@qq.com',user_type_id=3),
# Users(name='华容',email='39943@qq.com',user_type_id=4),
# Users(name='夏立光',email='39933@qq.com',user_type_id=1),
# Users(name='青面兽',email='39932@qq.com',user_type_id=2),
# Users(name='武松',email='39931@qq.com',user_type_id=3),
#
# ]
# session.add_all(obj2)
# session.commit()
# session.close()
# lsa=session.query(UserType).all()
# for row in lsa:
#     print(row.id,row.title)

# 分组 排序 链表 通配符 子查询 limit union where 原生sql


#条件查询
#单条查询
# ret=session.query(Users).filter_by(name='武松').all()
# #范围查询
# ret1=session.query(Users).filter(Users.id>2,Users.name=='武松').all()
# ret2=session.query(Users).filter(Users.id.between(1,4),Users.name=='松江').all()
# ret3=session.query(Users).filter(Users.id.in_([1,3,4])).all()
# ret4=session.query(Users).filter(-Users.id.in_([1,2])).all()
# ret5=session.query(Users).filter(Users.id.in_(session.query(Users.id).filter(Users.name=='武松')).all())
#
# #and_ or_
# from sqlalchemy import and_,or_
# ret6=session.query(Users).filter(and_(Users.id>3,Users.name=='武松')).all()
# ret7=session.query(Users).filter(or_(Users.id<4,Users.name=='松江')).all()
# ret8=session.query(Users).filter(
#     or_(Users.id<2,
#         and_(Users.name=='华容',Users.id>3),
#         Users.email !="")
# ).all()
#
#
#
# #通配符
# ret9=session.query(Users).filter(Users.name.like('李%')).all()
# ret91=session.query(Users).filter(Users.name.like('李_')).all()
# ret10=session.query(Users).filter(-Users.name.like('李%')).all()

#段制 limit  注意  顾头不顾尾 字符串切片
# ret11=session.query(Users)[1:3]
# # print([a.name for a in ret11])
# print(session.query(Users))

#排序
# ret12=session.query(Users).order_by(Users.name.desc()).all()
# ret13=session.query(Users).order_by(Users.name.desc(),Users.id.asc()).all()


#分组
# from sqlalchemy.sql import func
#
# ret=session.query(Users).group_by(Users.name).all()
# ret1=session.query(
#     func.max(Users.id),
#     func.sum(Users.id),
#     func.min(Users.id)
# ).group_by(Users.name).all()
#
# ret2=session.query(
#     func.max(Users.id),
#     func.sum(Users.id),
#     func.min(Users.id)
# ).group_by(Users.name).having(func.min(Users.id)>2).all()

#连表
#笛卡尔积
ret=session.query(Users,UserType).filter(UserType.id==Users.user_type_id).all()
print(ret)
# #join 默认使用外键关联
# ret1=session.query(UserType).join(Users).all()
# #左链接
# ret2=session.query(UserType).join(UserType,isouter=True).all()


# 子查询subquery()
# # ret=session.query(UserType.id,session.query(Users)).all()
# # ret1=session.query(UserType.id,session.query(Users).subquery()).all()
# # print(ret1)



#组合 union union_all
# q1 = session.query(Users.name).filter(Users.id > 2)
# q2 = session.query(UserType.title).filter(UserType.id < 2)
# ret = q1.union(q2).all()
#
# q1 = session.query(Users.name).filter(Users.id > 2)
# q2 = session.query(UserType.title).filter(UserType.id < 2)
# ret2= q1.union_all(q2).all()
# print(ret2)



