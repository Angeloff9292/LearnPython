num = [i for i in range(1, 21)]
res = []

def division(n):
        for n in range(1, n):
            for i in num:
                result = n%i
                
                if (result == 0):
                    res.append(n)
                
print(division(1000))
print(res)