﻿# Задание N3

# На берегу реки стояли n рыбаков, все они хотели перебраться на другой берег. Одна лодка может выдержать не более m килограмм,
# при этом в лодку помещается не более 2 человек. Определите, какое минимальное число лодок нужно, чтобы перевезти на другой берег
# всех рыбаков В первую строку вводится число m (1 ≤ m ≤ 10e6) - максимальная масса, которую может выдержать одна лодка. Во вторую строку
# вводится число n (1 ≤ n ≤ 100) - количество рыбаков. В следующие N строк вводится по одному числу Ai (1 ≤ Ai ≤ m) - вес каждого путешественника.
# Программа должна вывести одно число - минимальное количество лодок, необходимое для переправки всех рыбаков на противоположный берег.

# Метод для удобного запрашивания числа в заданном диапазоне
def askNumber(request, minValue, maxValue):
    while True:
        result = int(input(f'{request} (от {minValue} до {maxValue}): '))
        if result >= minValue and result <= maxValue:
            return result
        else:
            print('Вы ввели некорректное число. Попробуйте ещё раз...')

# В первую строку вводится число m (1 ≤ m ≤ 10e6) - максимальная масса, которую может выдержать одна лодка
m = askNumber('Введите максимальную массу, которую может выдержать лодка', 1, 10e6)

# Во вторую строку вводится число n (1 ≤ n ≤ 100) - количество рыбаков
n = askNumber('Введите число рыбаков', 1, 100)

# В следующие N строк вводится по одному числу Ai (1 ≤ Ai ≤ m) - вес каждого путешественника. Складываем их в массив
weights = []
for i in range(n):
    weight = askNumber(f'Введите вес рыбака №{i + 1}', 1, m)
    weights.append(weight)

# Сортируем массив по убыванию
weights = sorted(weights, reverse=True)

# Считаем требуемое количество лодок, сначала "засовывая в лодку" самых тяжелых пассажиров для оптимальной рассадки
boatsCount = 1
currentMass = 0
for weight in weights:
    currentMass += weight
    if currentMass > m:
        boatsCount += 1
        currentMass = weight

print(f'Чтобы перевезти всех рыбаков вам потребуется {boatsCount} лодок')
