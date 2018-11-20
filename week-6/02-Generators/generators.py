def chain(iterable_one, iterable_two):
    if iter(iterable_one) and iter(iterable_two):
        for i in iterable_one:
            yield i
        for j in iterable_two:
            yield j
    else:
        raise TypeError


def compress(iterable, mask):
    for index, value in enumerate(iterable):
        if isinstance(mask[index], bool):
            if mask[index] is True:
                yield value
        else:
            raise TypeError


def cycle(iterable):
    for index in iterable:
        yield index
