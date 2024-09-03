# Задание N2

# В Урок N10. Ранее вы создавали словарь с информацией о питомце. Теперь нам нужна "настоящая" база данных для ветеринарной клиники.
# Подробное описание требуемого функционала вынесено в файл readme.txt

# Создадим словарик для наших животных
pets = dict()

# Функция для добавления данных в БД
def db_create(name, category, age, ownerName):
    lastId = max(pets, key=pets.get) if len(pets.keys()) > 0 else 0
    currentId = lastId + 1
    pets[currentId] = dict()
    pets[currentId]['name'] = name
    pets[currentId]['category'] = category
    pets[currentId]['age'] = age
    pets[currentId]['ownerName'] = ownerName

# Функция для обновления данных в БД
def db_update(petId, name, category, age, ownerName):
    pets[petId]['name'] = name
    pets[petId]['category'] = category
    pets[petId]['age'] = age
    pets[petId]['ownerName'] = ownerName

# Функция для чтения данных из БД
def db_get(petId):
  return pets[petId] if petId in pets.keys() else False

# Функция для удаления записи из БД
def db_delete(petId):
    if petId in pets:
        del pets[petId]

# Обработчик команды create
def handleCreateCommand():
    name = input('Введите имя питомца: ')
    category = input('Введите тип питомца: ')
    age = int(input('Введите возраст питомца: '))
    ownerName = input('Введите имя владельца: ')
    # отправляем запрос в БД
    db_create(name, category, age, ownerName)

# Обработчик команды read
def handleReadCommand():
    petId = int(input('Введите id питомца: '))
    # Пробуем прочитать из БД
    pet = db_get(petId)
    if pet == False:
        print(f'Питомец с id {petId} не найден')
    else:
        printPet(pet)

# Обработчик команды update
def handleUpdateCommand():
    petId = int(input('Введите id питомца: '))
    name = input('Введите имя питомца: ')
    category = input('Введите тип питомца: ')
    age = int(input('Введите возраст питомца: '))
    ownerName = input('Введите имя владельца: ')
    # Пробуем обновить в БД
    pet = db_get(petId)
    if pet == False:
        print(f'Питомец с id {petId} не найден')
    else:
        db_update(petId, name, category, age, ownerName)

# Обработчик команды delete
def handleDeleteCommand():
    petId = int(input('Введите id питомца для удаления: '))
    # Пробуем удалить из БД
    db_delete(petId)
    print(f'Питомец с id {petId} удален')

# Функция для вывода информации о питомце на экран
def printPet(pet):
    name = pet['name']
    category = pet['category']
    age = pet['age']
    ownerName = pet['ownerName']
    print(f'{name} - {category}, {age} {getSuffix(age)}, владелец: {ownerName}')

# Функция, с помощью которой можно получить суффикс
def getSuffix(age):
  if age % 10 == 1:
      return 'год'
  if age % 10 < 5:
      return 'года'
  else:
      return 'лет'

# Эта функция создана для удобства отображения всего списка питомцев
def showPetsList():
    for petId in pets.keys():
        pet = db_get(petId)
        print(f'ID {petId} | ', end='')
        printPet(pet)

###

while True:
    print('\nСписок доступных команд: \n• create - создать запись о питомце \n• read - получить информацию о питомце по id\n• update - обновить информацию о питомце по id\n• delete - удалить питомца по id\n• list - отобразить информацию обо всех питомцах\n• stop - завершить работу\n')
    command = input('> ').lower()
    if command == 'create':
        handleCreateCommand()
    elif command == 'read':
        handleReadCommand()
    elif command == 'update':
        handleUpdateCommand()
    elif command == 'delete':
        handleDeleteCommand()
    elif command == 'list':
        showPetsList()
    elif command == 'stop':
        break
    else:
        print(f'Команда \'{command}\' не найдена')