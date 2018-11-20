from contextlib import contextmanager


@contextmanager
def context_manager(*args):
    text_error = ''
    some_message = ''
    if len(args) == 1:
        exceptions = str(args[0])
        text_error = 'asserts ' + exceptions + ' is raised'
    else:
        exceptions = str(args[0])
        some_message = args[1]
        text_error = 'asserts ' + exceptions + ' is raised and contains ' + some_message
    try:
        yield 'Yielded value'
    except Exception:
        print(text_error)


def do_something():
    raise Exception()


SomeException = Exception
with context_manager(SomeException, 'error_msg') as cm:
    do_something()
