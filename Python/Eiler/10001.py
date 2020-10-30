st = True
x = 1

while st:
    
    x +=1
    z = [i for i in range(x) if x%x == 0 and x%1 == 0]
    if len(z) == 10001:
        print(z)
        st = False

# решето Эратосфена