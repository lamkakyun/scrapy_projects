# -*- coding: utf-8 -*-
import sqlalchemy
import sqlalchemy.ext.declarative

BaseModel = sqlalchemy.ext.declarative.declarative_base()
class BookWordMap(BaseModel):
    __tablename__ = 'book_word_map'

    book_id = sqlalchemy.Column(sqlalchemy.Integer)
    word_id = sqlalchemy.Column(sqlalchemy.Integer)
