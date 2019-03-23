# -*- coding: utf-8 -*-
import sys, os, time
import queue
import threading
sys.path.append(os.path.abspath('../misc'))

import db_helper
from db_model.IPPool import IPPool
from db_model.IPOldPool import IPOldPool
import lam_tools

_now_time = int(time.time())

config = lam_tools.get_config()
max_fail = config['TOOL']['ip_proxy_max_fail']
check_time_span = config['TOOL']['ip_proxy_check_time_span']
select_size = config['DB']['limit']
thread_num = int(config['TOOL']['thread_num'])
ip_queue = queue.Queue()



def remove_fail_ip():
    db_session = db_helper.get_ip_pool_session()
    _query = db_session.query(IPPool.ip_port, IPPool.is_https).filter(IPPool.fail_num > max_fail)

    _count = _query.count()
    if _count == 0:
        print("no fail ip")
        return
    
    _query.delete()
    db_session.close()


def producer():
    db_session = db_helper.get_ip_pool_session()

    while True:
        if empty_queue_event.isSet():

            _check_time = _now_time - int(check_time_span)
            _query = db_session.query(IPPool).filter(IPPool.fail_num <= max_fail).filter(IPPool.uptime < _check_time)

            _count = _query.count()
            print('===================【rest count %d】====================' % _count)
            if _count == 0:
                print('all done')
                done_event.set()
                break

            data = _query.limit(select_size).all()
            for d in data:
                ip_queue.put((d.ip_port, d.fail_num))
                
            empty_queue_event.clear()

    print('%s exit!' % threading.currentThread().getName())
    db_session.close()
        

def consumer():
    db_session = db_helper.get_ip_pool_session()

    while not done_event.isSet():
        try:
            ip_info = ip_queue.get(block=True, timeout=5)
        except Exception as e:
            print(e)
            break
        

        if ip_queue.empty():
            print('-----------------queue is empty------------------')
            time.sleep(int(config['TOOL']['ip_proxy_timeout']) + 1)
            empty_queue_event.set()

        if not ip_info:
            print('get ip info fail')
            continue
        else:
            ip_port = ip_info[0]
            fail_num = ip_info[1]
            _ip, _port = ip_port.split(':')

            # print(ip_info)

            is_ok = lam_tools.check_ip_proxy_with_sock(_ip, int(_port), int(config['TOOL']['ip_proxy_timeout']))

            print(_ip, _port, '【bingo】' if is_ok else '*fail*')

            if is_ok:
                save_data = {'fail_num': 0, 'is_ok': 1, 'uptime': _now_time}
            else:
                save_data = {'fail_num': fail_num + 1, 'is_ok': 0, 'uptime': _now_time}

            db_session.query(IPPool).filter(IPPool.ip_port == ip_port).update(save_data)
            db_session.commit()

    print('%s exit!' % threading.currentThread().getName())
    db_session.close()


if __name__ == '__main__':
    remove_fail_ip()

    empty_queue_event = threading.Event()
    empty_queue_event.set()
    done_event = threading.Event()


    t_list = []
    p = threading.Thread(target=producer, name="producer")
    t_list.append(p)
    p.start()

    for i in range(thread_num):
        c = threading.Thread(target=consumer, name="consumer " + str(i))
        t_list.append(c)
        c.start()
    
    for t in t_list:
        t.join()
    
    print('main thread exit!')


    