﻿# Задание N2
# А теперь мы с тобой напишем форму ввода ответа на тест по биологии для студентов.
# Он должен запрашивать по порядку этапы развития человека (проверим твое умение гуглить, что тоже очень важно для программиста. )
# и в конце вывести все стадии, разделенные знаком =>, что будет означать постепенный переход от одного к другому. В следующих уроках
# мы дополним эту форму до полноценного теста, который будет проверять правильность ответов, а пока - начнем с малого. Напоминаем, что
# разделить эти данные тебе поможет команда sep внутри команды print, например, чтобы разделить переменные знаком + нужно ввести:
# print(a1, a2, a3, sep='+')
# Подсказка: последняя стадия развития - Homo sapiens sapiens.

# PS: Умение гуглить привело к различным вариантам ответа на вопрос "Сколько было этапов эволюции человека". Беру за основу это:
# В настоящее время выделяют следующие основные этапы эволюции человека:
# дриопитек - рамапитек – австралопитек – человек умелый – человек прямоходящий – неандертальский человек (палеоантроп) – неоантроп (это уже человек современного типа, homo sapiens).

print('Назовите все этапы эволюции человека (7 этапов)')
stage1 = input('Введите название первого этапа: ')
stage2 = input('Введите название этапа, следующего за ' + stage1 + ': ')
stage3 = input('Введите название этапа, следующего за ' + stage2 + ': ')
stage4 = input('Введите название этапа, следующего за ' + stage3 + ': ')
stage5 = input('Введите название этапа, следующего за ' + stage4 + ': ')
stage6 = input('Введите название этапа, следующего за ' + stage5 + ': ')
stage7 = input('Введите название этапа, следующего за ' + stage6 + ': ')
print('В результате у нас получается:')
print(stage1, stage2, stage3, stage4, stage5, stage6, stage7, sep=' => ')