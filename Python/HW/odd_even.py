ent = int(input('Enter numbers:\n')) 

for i in range(ent+1):
    if i%2==0:
        print(f'{i} is even')
    else:
        print(f'{i} is odd')