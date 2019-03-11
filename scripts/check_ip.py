# -*- coding: utf-8 -*-
import sys, os, time
import queue
import threading
sys.path.append(os.path.abspath('../misc'))

import db_helper
from db_model.IPPool import IPPool
import lam_tools

_now_time = int(time.time())

config = lam_tools.get_config()
max_fail = config['TOOL']['ip_proxy_max_fail']
check_time_span = config['TOOL']['ip_proxy_check_time_span']
select_size = config['DB']['limit']
thread_num = config['TOOL']['thread_num']

session = db_helper.get_ip_pool_session()

# step 1: 找出失败次数为 n 次的记录，删除
def step1():
    # (暂时不删吧)
    pass

# step 2: 检测 ip
# 多线程， thread 1 
def step2():

    def _build_queue():
    
        _check_time = _now_time - int(check_time_span)
        _query = session.query(IPPool).filter(IPPool.fail_num <= max_fail).filter(IPPool.uptime < _check_time)
        # count = _query.count()
        _queue = queue.Queue()

        data = _query.all()
        for d in data:
            _queue.put((d.ip_port, d.fail_num))
        
        return _queue
    
    def _run(q, db_session):
        _name = threading.currentThread().getName()
        print(_name, ' start')
        while (q.qsize() > 0):
            data = q.get()
            # ip_port = d[0]
            # fail_num = d[1]
            if data:
                _core_process(data, db_session)

    def _core_process(data, db_session):
        ip_port = data[0]
        fail_num = data[1]
        _ip, _port = ip_port.split(':')

        is_ok = lam_tools.check_ip_proxy_with_sock(_ip, int(_port), int(config['TOOL']['ip_proxy_timeout']))
        print(_ip, _port, '【bingo】' if is_ok else '*fail*')
    
        if is_ok:
            save_data = {'fail_num': 0, 'is_ok': 1, 'uptime': _now_time}
        else:
            save_data = {'fail_num': fail_num + 1, 'is_ok': 0, 'uptime': _now_time}
        
        db_session.query(IPPool).filter(IPPool.ip_port == ip_port).update(save_data)
        db_session.commit()
        
    _queue = _build_queue()
    for i in range(int(thread_num)):
        _name = "thread %d" % i
        # sqlalchemy 的session 创建的线程 和 使用的线程必须一直，否则报错,所以才创建多个session，提供多个线程
        db_session = db_helper.get_ip_pool_session()
        t = threading.Thread(target=_run, name=_name, args=(_queue, db_session))
        t.start()

if __name__ == '__main__':
    step1()
    step2()