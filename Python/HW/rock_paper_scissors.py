import random

diction = {'R': 0, 'P': 1, 'S': 2 }

total_dic = {0: 'Tie', 1: 'You win!', -2: 'You win!', -1: 'AI win!', 2: 'AI win!'}

while True:
    sys_print = random.choice(list(diction.keys()))
    sys_solution = diction.get(sys_print)

    user_solution = (diction.get(input('Enter solution: \n')))

    print(total_dic.get(user_solution-sys_solution))

    
    user_sel = input('Are you whant continue? \n')
        
    if user_sel == 'N':
        break