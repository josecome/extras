# *args vs **kwargs

def my_sum(*args): # Only values
    r = 0
    for x in args: # Unpacking operator (*)
        r += x
    return r

print(my_sum(1, 2, 3))


def concatenate(**kwargs): # Keys and values
    r = ''
    for v in kwargs.values():
        r += v + ' '
    return r

print(
    concatenate(
        a='Jose', b='Jaime', c='Come'
        )
)
