num = [i for i in range (1, 101)]

sqd_ammount = []

for i in num:
    sqd_ammount.append(i**2)

amount_sqd = sum(num)**2

print(amount_sqd-sum(sqd_ammount))