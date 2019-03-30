#coding:utf-8
import time

class GetTime(object):
    def get_system_time(self):
        print(time.time())
        print(time.localtime())
        new_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
        print(new_time)

gettime = GetTime()
gettime.get_system_time()
