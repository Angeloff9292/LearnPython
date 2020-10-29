num = [i for i in range(1, 11)]
res = {}
x = 1

def divis(x):
    for i in num:
        if x%i == 0:
            res[i] = x
            x+=1

divis(x)
print(res)