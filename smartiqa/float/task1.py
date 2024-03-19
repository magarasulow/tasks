# Напишите функцию to_float(num), которая преобразует
# любое число в число с плавающей точкой.
# Если в качестве аргумента передан другой тип данных,
# она возвращает «Невозможно преобразовать».
def to_float(num):
    if isinstance(num, (int, float)):
        result = float(num)
        return result
    else:
        return 'Невозможно преобразовать'


print(to_float(13))
print(to_float('number1'))
print(to_float(14.6))
