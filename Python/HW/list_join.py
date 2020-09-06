first_lst = [2, 24, 66, 124, 1, 8, 7, 11]
second_lst = [4, 2, 5, 0, 11, 36, 85]

first_odd = []
for i in first_lst:
    if i%2!=0:
        first_odd.append(i)

second_even = []
for i in second_lst:
    if i%2==0:
        second_even.append(i)

joined_list = first_odd + second_even