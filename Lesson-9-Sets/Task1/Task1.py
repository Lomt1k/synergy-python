# Задание N1

# В первую строку вводится число N – количество чисел (1 ≤ N ≤ 100000). Во вторую строку вводится через пробел N чисел, каждое не превышает 2*10e9 по модулю.
# Требуется выяснить, сколько среди этих чисел различных. Выведите число, равное количеству различных чисел среди данных.

# Используем уже привычный нам метод для удобного запрашивания числа в заданном диапазоне
def askNumber(request, minValue, maxValue):
    while True:
        result = int(input(f'{request} (от {minValue} до {maxValue}): '))
        if result >= minValue and result <= maxValue:
            return result
        else:
            print('Вы ввели некорректное число. Попробуйте ещё раз...')

# Добавим ещё метод для запрашивания сразу нескольких чисел в одной строке
def askNumbers(request, minValue, maxValue, count):
    while True:
        result = list(map(int, input(f'{request} (от {minValue} до {maxValue}): ').split()))
        if len(result) != count:
            print(f'Нужно было ввести {count} чисел... Попробуйте еще раз...')
        else:
            hasBadNumbers = False
            for el in result:
                if el < minValue or el > maxValue:
                    print(f'По крайней мере одно из введённых значений не удовлетворяет требованию: {minValue} <= Ai <= {maxValue}')
                    hasBadNumbers = True
            if not hasBadNumbers:
                return result


# В первую строку вводится число N – количество чисел (1 ≤ N ≤ 100000)
n = askNumber('Введите N', 1, 100_000)

# Во вторую строку вводится через пробел N чисел, каждое не превышает 2*10e9 по модулю.
numbers = askNumbers(f'Введите {n} чисел через пробел', -2*10e9, 2*10e9, n)

uniqueList = set(numbers)
print(f'Среди введённых вами чисел обнаружено {len(uniqueList)} уникальных')