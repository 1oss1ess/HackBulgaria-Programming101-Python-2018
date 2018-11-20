def accepts(*args_required):
    def accepter(func):
        def decorator(*args_value):
            if type(args_value[0]) is not args_required[0]:
                raise ValueError('Argument 1 of say_hello is not str!')
            if len(args_value) == 1:
                return func(args_value[0])
            else:
                return func(args_value[0], args_value[1])
        return decorator
    return accepter


@accepts(str)
def say_hello(name):
    return "Hello, I am {}".format(name)


print(say_hello('Hacker'))


@accepts(str, int)
def deposit(name, money):
    print("{} sends {} $!".format(name, money))
    return True


print(deposit("RadoRado", 10))
