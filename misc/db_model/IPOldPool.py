# -*- coding: utf-8 -*-
import sqlalchemy
import sqlalchemy.ext.declarative

BaseModel = sqlalchemy.ext.declarative.declarative_base()
class IPOldPool(BaseModel):
    __tablename__ = 'ip_pool'

    ip_port = sqlalchemy.Column("ip_port", sqlalchemy.String(20), primary_key = True)
    is_https = sqlalchemy.Column(sqlalchemy.Integer)
    uptime = sqlalchemy.Column(sqlalchemy.Integer)