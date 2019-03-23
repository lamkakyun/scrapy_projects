# -*- coding: utf-8 -*-

import sqlalchemy
import sqlalchemy.orm
import sqlalchemy.ext.declarative
import mix_config

from db_model.IPPool import IPPool

def get_ip_pool_session():
    """create ip pool sqlite session"""
    db_path = mix_config.MC_IP_DB
    engine = sqlalchemy.create_engine("sqlite:///" + db_path)
    DBSessinon = sqlalchemy.orm.sessionmaker(bind=engine)
    session = DBSessinon() 
    return session

# def get_ip_old_pool_session():
#     """create ip pool sqlite session"""
#     db_path = mix_config.MC_IP_OLD_DB
#     engine = sqlalchemy.create_engine("sqlite:///" + db_path)
#     DBSessinon = sqlalchemy.orm.sessionmaker(bind=engine)
#     session = DBSessinon() 
#     return session


def get_ip_proxy_list(size = 10):
    """获取有效的ip代理"""
    db_session = get_ip_pool_session()
    data = db_session.query(IPPool).filter(IPPool.is_ok == 1).limit(size).values(IPPool.ip_port)
    
    ret = []
    for d in data:
        ret.append(d)

    return ret