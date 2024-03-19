# Требуется создать функцию list_sort(lst), которая сортирует список чисел по убыванию их абсолютного значения.
def list_sort(lst):
    for i in range(len(lst)):
        minimum = lst[i]
        index_of_min = i
        for j in range(i + 1, len(lst)):
            if minimum > lst[j]:
                minimum = lst[j]
                index_of_min = j
        temp = lst[i]
        lst[i] = minimum
        lst[index_of_min] = temp
    return lst


print(list_sort([4, 7, 3, 9, 5, 9]))
