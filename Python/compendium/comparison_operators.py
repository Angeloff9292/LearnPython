# Оператор сравнения >
print(2 > 1)
print(2 > 2)
print(2 >= 2)
print(3 > 2)
print(3 >= 4)

# Оператор сравнения <
print(2 < 3)
print(2 < 2)
print(2 <=2)
print(2 < 1)

# Оператор сравнения равно
print(1 == 1)
print(1 == 2)

# Оператор сравнения НЕ равно
print(1 != 1)
print(1 != 2)

# Сравниваем строеки
print("string" == "string")
print("string" == "anoter string")
print("String" == "string") # Сравнение чувствительно к регистру

# Назначаем переменные
x = "String"
y = "string"

print(x.lower() == y.lower()) #Приводим к одному кейсу и сравниваем

print(1 < 2 < 3)
print(1 < 2 and 2 < 3)
print(1 > 2 and 2 < 3)
print(1 > 2 or 2 > 1)
print(1 > 2 or 2 > 3)