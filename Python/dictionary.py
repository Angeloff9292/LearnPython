# # назначаем значения                      Старый код с предыдущего курса.
# configs = {
#     "browser": "Safari",
#     "app": "google site",
#     "test": "smoke",
#     "log": True
# }

# # выводим определенной значение
# print(configs.get("browser"))

# # Выводим ключ
# for conf in configs:
#     print(conf)

# # выоводим значения
# for conf in configs.values():
#     print(conf)

# if "browser" in configs:
#     print("Exist")

# Создаем словарь
players = {
    'Carlsen': 2842,
    'Caruana': 2822,
    'Mamedyrov': 2801,
    'Ding': 2797,
    'Giri': 2780
}

# players = dict(Carlsen=2842) - еще один вариант синтаксиса для сохдания списка

# Ищем елемент по ключу
top1 = players['Carlsen']
print(f"Top chess player's rating is {top1}")

# Ищем елемент по ключу
players.get('Carlsen')

# Добавляем елемент
players['So'] = 2780
print(players)

# Удаляем елемент по ключу
del players['So']
print(players)

# Выводим только ключи
keys = players.keys()
print(keys)
print(type(keys))

# Конвертируем в список
playersList = list(players.keys())
print(playersList)
print(type(playersList))

# Сортировка
print(sorted(players.keys()))

# Проверка на True/False
print('Carlsen' in players)
print('Kramnik' not in players)

# Выводим значения и конвертируем в список
print(players.values())
valuesList = list(players.values())
print(valuesList)

# цикл для вывода всех позиций из списка
for key, value in players.items():
    print(key, value)

# Удалить по ключу (без аргумента удалится последний)
players.pop('Giri')

#Удалить перввый
players.popitem()

# Длина словаря
len(players)

# Добавить ключ если он будет не найден и установить дефолтное значение None
players.setdefault('Karjakin')
print(players)