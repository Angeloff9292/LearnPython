x = 0

# while x <= 3:
#     print(f'x equal {x}')
#     x+=1

while x <= 3:
    print(f'x equal {x}')
    x+=1
else:
     print('Done.')

vals = range(0, 10)
sum = 0

for v in vals:
    if v%2 == 0:
        continue
    else:
        sum +=v
    if sum > 10:
        break
print(sum)