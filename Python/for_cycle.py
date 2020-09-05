numbersInt = [1, 2, 3, 4, 5, 6]
print(numbersInt)

# проходимся по спискам и выоводим каждое значение в итерации  
for i in numbersInt:
    print(i)

numbersRange = range(1, 5)
print(type(numbersRange))

for i in numbersRange:
    print(i)

for i in range(1, 10):
    print(i*i)

# В циклы можно вулючать булевые выражения
for i in range(1, 6):
    if i % 2 ==0:
        print(f'{i} is even')
    else:
        print(f'{i} is not even')

numbersNew = [1, 3, 7, 9]

for i, item in enumerate(numbersNew):
     numbersNew[i] *= 2
print(numbersNew)

# Можно использовать для строк
name = 'John'
for l in name:
    print(l)

# Можно генерировать данные
for _ in range(1, 5):
    print("Alalrm!")

# Можно использовать для кортежей
person = ('John', 'Silver', 22)

for p in person:
    print(p)

# Кортежи можно расковать
persons = [('John', 22), ('Bill', 34), ('Mary', 35)]

for (name, age) in persons:
    print(f'{name} is {age} years old')

# Можно использовать для словарей
players = dict(Carlsen=2842, Caruana=2822, Mamedyarov=2201)

for i in players.items():
    print(i)

# Можно распаковывать словари
for k, v in players.items():
    print(f'{k} have rating {v}')
 
# Можно использовать вложенные циклы (ппроверям числа которые в сумме дают ноль)
list1 = [2, 4, -5, 6, 8, -2]
list2 = [2, -6, 8, 3, 5, -2]

pairs =  []

for x in list1:
    for y in list2:
        cur_sum = x+y
        if cur_sum == 0:
            pairs.append((x, y))

print(pairs)