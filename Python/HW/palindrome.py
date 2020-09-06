enter1 = int(input(""))
enter = enter1

result = 0

while enter != 0:
    result = (result*10) + (enter%10)
    enter = int(enter/10)

if enter1 == result:
    print('Palindrome')
else:
    print('Not palindrome')