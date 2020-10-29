# Просто строка
a = "I`m Oleg"
print(a)

# Строка со скобками
b = 'Go to the "Haven"'
print(b)

# Строка с разными скобками
c = "I`m Oleg, go with me to the \"Haven\""
print(c)

# Строка со слешем
d = "C:\\User\\Documents"
print(d)

# Упрощенный тип слеша
e = r'C:\User\Documents'
print(e)

#С новой строки без картеки
f = "I`m Oleg. \nGo with me to the haven"
print(f)

#С новой строки с кареткой
g = "I`m Oleg. \r\nGo with me to the haven"
print(g) 
print(g[0]) # Первый символ инедексации
print(g[-5]) # Ппятый с конца символ инедексации
print(g[2:]) # Начиная с третьего символа
print(g[2:8]) # Со второго по восьмой
print(g[::2]) # Каждый второй симовл
print(g[3:15:2]) # Каждый второй с третьго по пятнадцатый

#Сложенеи строк через +
p = "I`m" + " " "Oleg"
print(p)

# Сложение строк
hello = "Hello" #Назначение переменных
world = "world"
print("%s %s" %(hello, world)) # Через плейсхолдер
print("{} {}" .format(hello, world)) # Через функцию .format

# Множитель символов
k = "p"*7
print(k)
