print("My name is {}".format("Oleg")) # Заполняет плейсхолдеры 

my_name = "Oleg"
old = 28
print("My name is {}, and I`m {}".format(my_name, old)) # Выводит все по порядку
print("My name is {1}, and I`m {0}".format(my_name, old)) # Можно заменять плейсхолдеры индексами

pi = 3.141567893
print("PI is uqual {pi:1.3f}".format(pi=pi)) # Вставляем аргументы в плейсхолдер

print(f"My name is {my_name} and I`m {old}") # Новый способ форматирования строк (интерполяция строк)
 
