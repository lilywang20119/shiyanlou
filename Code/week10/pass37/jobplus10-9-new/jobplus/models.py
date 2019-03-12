from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask import url_for

from werkzeug.security import generate_password_hash,check_password_hash

from flask_login import UserMixin,current_user

# 注意这里不再传入 app 了
db = SQLAlchemy()
#中间表


class Base(db.Model):
    #不需要创建表
    __abstract__ = True
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

user_job = db.Table(
    'user_job',Base.metadata,
    db.Column('user_id',db.Integer,db.ForeignKey('user.id',ondelete='CASCADE')),
    db.Column('job_id',db.Integer,db.ForeignKey('job.id',ondelete='CASCADE'))
)

'''
resume_job = db.Table(
    'resume_job',
    db.Column('resume_id',db.Integer,db.ForeignKey('resume.id')),
    db.Column('job.id',db.Integer,db.ForeignKey('job.id'))
)
'''


class User(Base,UserMixin):
    __tablename__ = 'user'

    ROLE_USER = 10
    ROLE_COMPANY = 20
    ROLE_ADMIN = 30


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True, index=True, nullable=False)
    email = db.Column(db.String(64),unique=True,index=True,nullable=False)
    _password = db.Column('password',db.String(256),nullable=False)
    role = db.Column(db.SmallInteger,default=ROLE_USER)
    is_disable = db.Column(db.Boolean,default=False)
    # 一对一的关系
    resume = db.relationship('Resume',uselist=False,cascade='all,delete-orphan',backref='user')
    collect_jobs = db.relationship('Job',secondary=user_job)
    upload_resume_url = db.Column(db.String(64))

    #企业用户详情
    companydetail = db.relationship('CompanyDetail',uselist=False,cascade='all,delete-orphan',backref='user')


    def __repr__(self):
        return '<User:{}>'.format(self.name)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self,orig_password):
        self._password = generate_password_hash(orig_password)

    def check_password(self,password):
        return check_password_hash(self._password,password)

    @property
    def is_admin(self):
        return self.role == self.ROLE_ADMIN

    @property
    def is_company(self):
        return self.role == self.ROLE_COMPANY

    @property
    def is_staff(self):
        return self.role == self.ROLE_USER



class CompanyDetail(Base):
    __tablename__ = 'companydetail'

    id = db.Column(db.Integer,db.ForeignKey('user.id',ondelete='CASCADE'),primary_key=True)
    image_url = db.Column(db.String(256))
    finance = db.Column(db.String(64))
    staff_num = db.Column(db.String(64))
    type = db.Column(db.String(64))
    about = db.Column(db.Text)
    def __repr__(self):
        return '<CompanyDetail:{}>'.format(self.about[:9])


class Job(Base):
    __tablename__ = 'job'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    salary = db.Column(db.String(64))
    location = db.Column(db.String(32))
    tags = db.Column(db.String(64))
    experience_requirement = db.Column(db.String(64))
    degree_requirement = db.Column(db.String(64))
    is_fulltime = db.Column(db.Boolean,default=True)
    release_time = db.Column(db.String(64))
    #是否在招聘
    is_open = db.Column(db.Boolean,default=True)
    is_disable = db.Column(db.Boolean,default=False)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Job:{}>'.format(self.name)

    @property
    def current_user_is_applied(self):
        d = Delivery.query.filter_by(job_id=self.id,resume_id=current_user.id).first()
        return d is not None



class Resume(Base):
    __tablename__ = 'resume'

    id = db.Column(db.Integer,db.ForeignKey('user.id',ondelete='CASCADE'),primary_key=True)
    name = db.Column(db.String(32),nullable=False)
    age = db.Column(db.SmallInteger)
    work_age = db.Column(db.SmallInteger)
    home_city = db.Column(db.String(64))
    job_experience = db.Column(db.Text)
    edu_experience = db.Column(db.Text)
    project_experience = db.Column(db.Text)
    resume_url = db.Column(db.String(128))


class Delivery(Base):
    __tablename__ = 'delivery'

    #等待企业审核
    STATUS_WAITING = 1
    #被拒绝
    STATUS_REJECT = 2
    #被接受等待面试通知
    STATUS_ACCEPT = 3

    id = db.Column(db.Integer,primary_key=True)
    job_id = db.Column(db.Integer,db.ForeignKey('job.id',ondelete='SET NULL'))
    user_id = db.Column(db.Integer,db.ForeignKey('user.id',ondelete='SET NULL'))
    status = db.Column(db.SmallInteger,default=STATUS_WAITING)
    #企业回应
    response = db.Column(db.String(256))
