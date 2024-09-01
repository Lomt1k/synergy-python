# Задание N1

# Сначала вводится число N, затем вводится ровно N целых чисел. Подсчитайте, сколько из них равны нулю, и выведите это количество.

numbersCount = int(input('Введите число N: '))
zeroCount = 0
for i in range(0, numbersCount):
    value = int(input('Введите число: '))
    if value == 0:
        zeroCount += 1

print(f'Нуль был введён {zeroCount} раз')
