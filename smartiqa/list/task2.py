# Напишите функцию change(lst), которая принимает список
# и меняет местами его первый и последний элемент.
# В исходном списке минимум 2 элемента.
def change(lst):
    n = len(lst)
    first = lst[0]
    lst[0] = lst[n - 1]
    lst[n - 1] = first
    return lst


print(change([1, 2, 3, 4, 5]))
