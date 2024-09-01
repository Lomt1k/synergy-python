﻿# Задание N2

# Дано слово из маленьких латинских букв. Сколько там согласных и гласных букв? Гласными называют буквы «a», «e», «i», «o», «u».
# Для решения задачи создайте переменную и в неё положите слово с помощью input()
# А также определите количество каждой из этих гласных букв Если какой-то из перечисленных букв нет - Выведите False

# PS: В задаче ничего не сказано про букву 'y', я её также добавил к согласным

a = 0
e = 0
i = 0
o = 0
u = 0
y = 0
vowels = 0
consonants = 0

word = input('Введите слово латинскими прописными буквами: ')
for char in word:
    if char == 'a':
        a += 1
        vowels += 1
    elif char == 'e':
        e += 1
        vowels += 1
    elif char == 'i':
        i += 1
        vowels += 1
    elif char == 'o':
        o += 1
        vowels += 1
    elif char == 'u':
        u += 1
        vowels += 1
    elif char == 'y':
        y += 1
        vowels += 1
    else:
        consonants += 1

print('Гласных:', vowels)
print('Согласных:', consonants)
print('Букв \'a\':', a)
print('Букв \'e\':', e)
print('Букв \'i\':', i)
print('Букв \'o\':', o)
print('Букв \'u\':', u)
print('Букв \'y\':', y)