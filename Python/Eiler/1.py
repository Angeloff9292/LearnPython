def even_or_odd(s):
    ever_odd = []
    odd = []
    even = []
    for l in s:
        ever_odd.append(l)
        ever_odd = list(map(int, ever_odd))
    for i in ever_odd:   
        if i%2 == 0:
            even.append(i)
        else:
            odd.append(i)
    
    if sum(odd) == sum(even):
        res = "Even and Odd are the same"
    elif sum(odd) > sum(even):
        res = "Odd is greater than Even"
    elif sum(odd) < sum(even):
        res = "Even is greater then Odd"    
    
    return res

print(even_or_odd("12"))