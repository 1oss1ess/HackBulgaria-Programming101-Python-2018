class Log:
    def __init__(self, exception, msg=None):
        self.exception = exception
        self.msg = msg

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            return
        if exc_val is ValueError:
            return
        return True


def do_something():
    raise Exception('SomeExcept')


with assertRaises(Exception):
    do_something()
