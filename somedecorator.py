import functools
import time


def run_time(fn):
    '''
    程序运行时长
    '''
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        start = time.time()
        res = fn(*args, **kw)
        print('%s 运行了 %f 秒' % (fn.__name__, time.time() - start))
        return res
    return wrapper
