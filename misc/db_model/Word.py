# -*- coding: utf-8 -*-
import sqlalchemy
import sqlalchemy.ext.declarative

BaseModel = sqlalchemy.ext.declarative.declarative_base()
class Word(BaseModel):
    __tablename__ = 'word'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key = True)

    word = sqlalchemy.Column(sqlalchemy.Text)
    cn_comment = sqlalchemy.Column(sqlalchemy.Text)
    en_comment = sqlalchemy.Column(sqlalchemy.Text)