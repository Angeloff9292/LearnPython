players = [('Carlsen'), 1990, 2842], ('Caruana', 1992, 2822), ('Mamedyarov', 1985, 2801)
print(players[0])

from collections import namedtuple

Player = namedtuple('Player', 'Name Age Rating') # Создаем класс

# создаем именованный кортеж
players = [Player('Carlsen', 1990, 2842), Player('Caruana', 1992, 2822), Player('Mamedyarov', 1985, 2801)]

#Выводим все ппо первому индексу
print(players[0])

# Выводим тоолько имя по первоу индексу
print(players[0].Name)