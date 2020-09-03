import os
dirpath = os.getcwd() #выводим текущую директорию
print(dirpath)

with open('test_file_name.txt', 'w') as f:
    f.write('Name|Phone\nJohn;1234\nBob;9378\nElice;9432')  # Создаем файл и записываем данные, в данном случае файл закрывается автоматически

# Открываем файл
file = open('test_file_name.txt')
print(file)

# Читаем файл
data = file.read()
print(data)

# Переводим картеку в начало файла
file.seek(0)
print(file.read())

# Выводим тип данных в файле
file.seek(0)
print(type(file.read()))

# Разбиваем файл на строки
file.seek(0)
lines = file.readlines()
print(type(lines))
print(lines)

# Открываем файл по указанному пути
sample_file = open('/Users/olegzalipsky/Documents/LearnPython/test_file_name.txt')
print(sample_file)

# Закрываем файлы
f.close()
file.close()
sample_file.close()

# Прооверяем на закрытие
print(f.closed)
print(file.closed)
print(sample_file.closed)

# Аргуементы файлов
# r - чтение (должен существовать, режим по умолчанию )
# w - запись (создаться новый, если не существует, если не существует - то перезапишет)
# a - добавление в конец файла (должен существовать, новый не создается)
# r+ - и чтение и запись (должен существовать, новый не создается)
# w+ - и чтение и запись (перезапишет если существовал, создаст новый если не существовал)

# Открываем файл на чтение и на запись
with open('test_file_name.txt', "r+") as file:
    file.seek(0, 2) # Перемещаем картеку в конец
    file.write('\nEdgar;8903') # Делаем запись с новой строки
    file.seek(0) # Перемещаем каретку в начало
    print(file.read()) # Читаем файл

# Проверям файл на закрытие
if(file.closed) == True :
    print ("File is closed")
else:
    file.close()