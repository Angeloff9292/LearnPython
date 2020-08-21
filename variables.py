name: str = "John"
sallary: int = 999
isMarried: bool = True

#Можно не описывать тип переменной

name = "John" #string
sallary = 999 #int
isMarried = True #boolean

#Можно соеденить 2 стринги "test"+"test". Разные типы переменных выводятся через запятую

print("Hello ", name, "!")
print("My amount is" , sallary)
print("Im married?", isMarried)

# Что бы вывести тип переменной

print(type(name)) #str
print(type(sallary)) #int
print(type(isMarried)) #bool

