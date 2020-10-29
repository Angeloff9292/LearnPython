# создаем пустое множество
myset = set()
print(myset)

print(type(myset))

# Добавляем елементы
myset.add(1)
print(myset)

myset.add(2)
print(myset)

# Вторая цифра 2 не добавится, множество хранит только уникальные значения
myset.add(2)
print(myset)

# Создаем список и конвертируем в множество
my_list = [1, 1, 1, 1, 1, 4, 4, 3, 4, 4, 4, 4, 4, 2, 2, 2, 2, 2, 1, 1, 4]
s = set(my_list)

# Выводим длинну множества и само множество
print(len(s))
print(s)  

# Проверяем наличие цифр во множестве
print( 1 in s)
print(8 in s)

# Создаем новые множества
set1 = {1,2,3,4}
set2 = {1,2,3,4,5}

# Проверяем на сабсет
print(set1.issubset(set2))

# Проверяем на суперсет
print(set2.issuperset(set1))

#соединяем сеты
print(set1.isdisjoint(set2)) 

set1 = {1,2,3}
set2 = {4,5,6}

print(set1.isdisjoint(set2)) 

# Включаем один сет в другой
set3 = set1.union(set2)
print(set3)

# Добавляем недостающие елементы
set1 = {1,2,3,4}
set2 = {1,2,3,4,5,6}
set4 = (set1.intersection(set2))
print(set4)

# Выводим разницу между множествами
set5 = (set1.difference(set2))
print(set5)

# Выводим разницу симетрически
set6 = (set1.symmetric_difference(set2))
print(set6)

# Обновлям одно множество до другого
set1.update(set2)
print(set1)

#Удалям елемент множества
set1.remove(1)
print(set1)
set1.discard(42)