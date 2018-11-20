import time


def sleep(seconds):
    return time.sleep(seconds)


def performance(file):
    def accepter(func):
        def decorator(*args, **kwargs):
            t1 = time.time()
            result = func(*args, **kwargs)
            t2 = '%.2f' % (time.time() - t1)
            with open(file, 'a') as f:
                f.write('{} was called and took {} seconds to complete\n'.format(func.__name__, t2))
            return result
        return decorator
    return accepter


@performance('log.txt')
def something_heavy():
    sleep(2)
    return "I am done!"


print(something_heavy())
