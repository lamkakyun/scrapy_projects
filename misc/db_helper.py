# -*- coding: utf-8 -*-

import sqlalchemy
import sqlalchemy.orm
import sqlalchemy.ext.declarative
import mix_config


def get_ip_pool_session():
    """create ip pool sqlite session"""
    db_path = mix_config.MC_IP_DB
    engine = sqlalchemy.create_engine("sqlite:///" + db_path)
    DBSessinon = sqlalchemy.orm.sessionmaker(bind=engine)
    session = DBSessinon() 
    return session