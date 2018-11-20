import traceback


# traceback.print_stack()
# print(repr(traceback.extract_stack()))
# print(repr(traceback.format_stack()))
an_error = IndexError('tuple index out of range')
asd = traceback.format_exception_only(type(an_error), an_error)
asd.append(Exception('SomeException'))
# print(asd)

from contextlib import contextmanager


@contextmanager
def rnd_manager(*args, **kwargs):
    print(args)
    print(kwargs)
    print('Enter')

    yield 'yield value'
    print('Exit')


with rnd_manager('arg1', gh=43) as v:
    print(v)
    print('Insaide')
