new_arr = []
for i in range (0, 1000):
    if i%3 == 0 or i%5 == 0:
        new_arr.append(i)
print(sum(new_arr))