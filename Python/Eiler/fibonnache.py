fib = [0]
new_fib = []

fib1 = 1
fib2 = 1

amount = 4000000

while (max(fib) <= amount):
    fib_sum = fib2 + fib1
    fib1 = fib2
    fib2 = fib_sum

        
    if fib_sum <= amount:
        fib.append(fib_sum)
    else:
        break

for i in fib:
    if i%2 == 0:
        new_fib.append(i)

print(sum(new_fib))