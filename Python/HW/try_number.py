import random

sys_number = random.randint(1, 50)

for i in range(1, 7):
    user_number = int(input('Enter number: \n'))
    if user_number == sys_number:
        print('Ok')
        break
    elif user_number > sys_number:
        print ('Lower number')
    else:
        print('Upper number')
        