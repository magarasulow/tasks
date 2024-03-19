# На входе имеем список строк разной длины.
# Необходимо написать функцию all_eq(lst),
# которая вернет новый список из строк одинаковой длины.
# Длину итоговой строки определяем исходя из самой большой из них.
# Если конкретная строка короче самой длинной,
# дополнить ее нижними подчеркиваниями с правого края до требуемого количества символов.
#
# Расположение элементов начального списка не менять.
def all_eq(words: list) -> list:
    maximum = len(words[0])
    for word in range(1, len(words)):
        current_length = len(words[word])
        if current_length > maximum:
            maximum = current_length

    result = []
    for word in words:
        lacks = maximum - len(word)
        for i in range(0, lacks):
            word += '_'
        result.append(word)

    return result


print(all_eq(['Привет', 'Хуй', 'Член']))
