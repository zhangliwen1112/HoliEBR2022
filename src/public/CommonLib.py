import datetime
import time
import threading


class CommonLib:
    def __init__(self):
        pass

    @classmethod
    def getcurrenttime(cls):
        currenttime = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        return currenttime
    @classmethod
    def getcurrentcay(cls):
        currentday = datetime.datetime.now().strftime('%Y-%m-%d')
        return currentday
    @classmethod
    def getcurrenttime1(cls):
        currenttime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return currenttime

    @classmethod
    def getyesterdaytime(cls):
        # now_time = datetime.datetime.now()
        # yes_time = now_time + datetime.timedelta(days=-1)
        # yes_time_yes = yes_time.strftime('%Y-%m-%d %H:%M:%S')
        yes_time = (datetime.datetime.now()+ datetime.timedelta(days=-1)).strftime('%Y-%m-%d %H:%M:%S')
        return yes_time
    @classmethod
    def getyesterday(cls):
        yes_time = (datetime.datetime.now() + datetime.timedelta(days=-1)).strftime('%Y-%m-%d')
        return yes_time

    @classmethod
    def sleep(cls, p_time):
        time.sleep(p_time)

if __name__ == '__main__':
    res = CommonLib.getyesterdaytime()
    print(res)
