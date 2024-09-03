# Задание N2

# Дана строка, длина которой не превосходит 1000. Вам требуется преобразовать все идущие подряд пробелы в один. Выведите измененную строку.

text = input('Введите строку, из которой вы хотите убрать лишние пробелы (более одного пробела подряд): ')
canUseSpace = True
for char in text:
    if char == ' ':
        if canUseSpace:
            print(char, end='')
            canUseSpace = False
    else:
        canUseSpace = True
        print(char, end='')
print()