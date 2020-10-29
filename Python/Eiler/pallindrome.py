numbers_and_amount = {}

min_arr = [i for i in range(1, 101)]
max_arr = [i for i in range(1, 1000)]
    
for i in max_arr:
    for j in min_arr:
        amount = i*j
        if (str(amount) == str(amount)[::-1]):
            numbers_and_amount[amount] = (str(i)+"*"+str(j))

print(numbers_and_amount.get(max(list(numbers_and_amount.keys()))))