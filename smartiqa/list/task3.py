# Функция to_list() принимает неограниченное количество параметров.
# Обработайте их так, чтобы на выходе получить список из этих элементов.
def to_list(*xyi):
    result = []
    for i in xyi:
        result.append(i)
    return result


print(to_list(5, 2, 7, 35, 244565, 5, 766, 45, 3))
