# Функция mul_to_int(a, b) может принимать целые или вещественные числа.
# Если результат умножения аргументов не имеет значимых чисел после запятой,
# то она возвращает его в виде целого числа. В противном случае – в виде float.
def mul_to_int(a, b):
    result = a * b
    int_result = int(result)
    if result - int_result == 0:
        return int_result
    else:
        return result


print(mul_to_int(4, 6.7))
print(mul_to_int(4, 5.0))
