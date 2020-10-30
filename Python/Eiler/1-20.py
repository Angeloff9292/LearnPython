x = 1

status = True

while status:
    z = []
    z=[i for i in range (21,1, -1) if x%i==0]
    if len(z) == 20:
        print(x)
        status = False
    x+=1