# Николай задумался о поиске «бесполезного» числа на основании списка.
# Суть оного в следующем: он берет произвольный список чисел,
# находит самое большое из них, а затем делит его на длину списка.
# Студент пока не придумал, где может пригодиться подобное значение,
# но ищет у вас помощи в реализации такой функции useless(s).
def useless(s: list):
    return max(s) / len(s)


print(useless([4, 6, 3, 1, 6, 45, 33, 9]))
