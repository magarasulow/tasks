# Определите функцию foo(a),
# которая возвращает результат целочисленного
# и по модулю деления любого целого числа на -11.
def foo(a):
    return a // -11, a % -11


print(foo(22))


def foo_1(a):
    return divmod(a, -11)


print(foo_1(22))