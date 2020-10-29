int_list = [1, 2, 3,] # Список чисел
mix_list = [1, 2.0, 'string'] # Смешанный список
print(len(int_list)) # длинна списка
print(int_list[0]) # Вывод позиции по индексу
print(int_list[-1]) # Вывод позиции по индексу с конца
print(int_list[1:]) # Вывод позиций начиная со 2

names1 = ['John', 'Bob', 'Elias']
names2 = ['Tracy', 'Mason', 'Billy']
nameesCombined = names1+names2 # Конкастинация списков

nameesCombined[1]='Willian' # Замена позиции по индексу

nameesCombined.append('Tomas') # Добавление записи в список

popped = nameesCombined.pop() # Удаление последнего елемента

print(popped)

popped1 = nameesCombined.pop(2) # Удаление елемента по индексу
print(nameesCombined)

letters = ['ab', 'ac', 'aa']
letters.sort() # Сортировка списка
print(letters)

letters1 = ['abc', 'a', 'ab']
letters1.sort(key=len) # Сортировка по длине
print(letters1)

numbers = [1, 2, 3,56,14,64,12,66,11,]
print(numbers)
numbers.sort()
print(numbers)
numbers.reverse() # Вывод списка наоборот
print(numbers)
numbers.sort(reverse=True) # Сортировка наоборот

numbers.insert(1, 22) # Добавление значения после 2 елемента
print(numbers)

print(numbers.index(56)) # Вывести индекс числа 5
print(numbers.count(3)) # Посичтать количество числа 3
copy = numbers.copy() # Копия списка
print(copy)

numbers.clear() # Очистить список
print(numbers) 
