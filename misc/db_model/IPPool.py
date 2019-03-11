# -*- coding: utf-8 -*-
import sqlalchemy
import sqlalchemy.ext.declarative

BaseModel = sqlalchemy.ext.declarative.declarative_base()
class IPPool(BaseModel):
    __tablename__ = 'ip_pool'

    ip_port = sqlalchemy.Column("ip_port", sqlalchemy.String(20), primary_key = True)
    is_ok = sqlalchemy.Column(sqlalchemy.Integer)
    is_https = sqlalchemy.Column(sqlalchemy.Integer)
    hide_level = sqlalchemy.Column(sqlalchemy.Integer)
    fail_num = sqlalchemy.Column(sqlalchemy.Integer)
    uptime = sqlalchemy.Column(sqlalchemy.Integer)
    