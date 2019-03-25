# -*- coding: utf-8 -*-
import sqlalchemy
import sqlalchemy.ext.declarative

BaseModel = sqlalchemy.ext.declarative.declarative_base()
class Book(BaseModel):
    __tablename__ = 'book'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key = True)

    book_name = sqlalchemy.Column(sqlalchemy.Text)
    book_desc = sqlalchemy.Column(sqlalchemy.Text)