# Так как в Python операции с вещественными числами
# могут давать неожиданные результаты
# (в частности, 0.1 + 0.2 не будет в точности равняться 0.3),
# стоит задача с этим как-то справляться.
# Требуется написать функцию eqv(a, b, c), которая принимает 3 числа.
# Числа a и b складываются.
# Затем эта сумма сравнивается с числом "с" с определенной степенью точности.
# Точность равняется 0.01 % от большего из чисел a и b.
# Функция вернет True, если выполняется равенство, иначе False.
def eqv(a, b, c):
    result = a + b
    result1 = 0.01 / 100
    result2 = result1 * max(abs(a), abs(b))
    return abs(result - c) <= result2


print(eqv(5.16, 0.11, 2.1))
print(eqv(0.12, 0.31, 0.43))