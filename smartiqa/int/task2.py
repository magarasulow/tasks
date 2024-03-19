# Сколько мегабайт памяти занимает число 3 ** 9090001?
# Для решения воспользуйтесь функцией getsizeof() из модуля sys.
import sys

result = 3 ** 9090001
size = sys.getsizeof(result)
print(size)
