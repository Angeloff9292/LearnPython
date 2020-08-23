name = "John"
sallary = 999
isMarried = True 
# Если name = oleg выводим valid, любое другое - not valid
if (name == "Oleg"):
   print("Valid")
else:
  print("Not valid")

# Можно добавлять через оператор ИЛИ
if (name == "Oleg" or isMarried == False):
   print("Valid")
else:
  print("Not valid")

# Можно добавлять через оператор И
if (name == "Oleg" and isMarried == False):
   print("Valid")
else:
  print("Not valid")

# Используется оператор else if
if (sallary == 1000):
    print("sallary is 1000")
elif (sallary > 1000):
    print("Sallary is more 1000")
else:
    print("Sallary is less 1000")