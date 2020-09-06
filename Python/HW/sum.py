ent = int(input('Enter number: \n'))
numb=[]

for i in range(ent+1):
    if i%3==0 or i%5==0:
        numb.append(i)

print(sum(numb))