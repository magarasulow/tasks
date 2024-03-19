# Николай решил вспомнить старые времена.
# В свое время было модно писать сообщения
# с чередующимися заглавной и малой буквами.
# Он захотел изобрести функцию,
# которая будет делать с любой предоставленной строкой аналогичное.
# Ваша задача:
# повторить труд студента camel(st) с учетом того,
# что пробелы и знаки препинания не должны портить чередование регистра
# символов (они в этом процессе не учитываются, но возвращаются в итоговой строке).
def camel(st):
    result = ''
    result1 = 0
    for index, i in enumerate(st):
        if i.isalpha():
            if result1 % 2 == 0:
                result += i.upper()
            else:
                result += i.lower()
            result1 += 1
        else:
            result += i
    return result


print(camel('Я ебал осла в рот'))