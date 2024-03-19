# Напишите функцию num_sum(a), принимающую любое значение.
# Если это целое число, то возвратить сумму его чисел.
# В противном случае возвращается фраза «Это не целое число».
def num_sum(a):
    if isinstance(a, int):
        result = str(abs(a))
        a = 0
        for i in result:
            a += int(i)
        return a
    return 'Это не целое число'


print(num_sum(-146))
print(num_sum('xyi'))
