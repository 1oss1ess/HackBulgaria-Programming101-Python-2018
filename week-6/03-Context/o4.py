from contextlib import contextmanager
import time


@contextmanager
def assertRaises(exception, msg=None):
    try:
        yield
    except Exception as exc:
        if not isinstance(exc, exception):
            print('Expected {}, got {}'.format(exception.__name__, exc.__class__.__name__))
            raise exc
        if msg:
            err_msg = str(exc)
            if err_msg != msg:
                print('Expected {} message, got {}'.format(msg, err_msg))
                raise exc
    else:
        print('{} was not raised.'.format(exception.__name__))


def do_smt():
    return
    raise TypeError('asd')


with assertRaises(TypeError, 'qwe'):
    do_smt()
