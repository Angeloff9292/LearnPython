x = int(input("Enter you number:"))

array = []

for i in range(1, x+1):
    if i%3 == 0 or i%5 == 0:
        array.append(i)
    else:
        continue

print(sum(array)) 