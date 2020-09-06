current_hand = [2, 3, 4, 10, 'Q', 5]

sums = 0
for i in current_hand:
    if i == 2 or i == 3 or i == 4 or i == 5 or i == 6:
        sums+= 1 
    elif i == 7 or i == 8 or i == 9:
        sums+= 0
    elif i == 10 or i == 'J' or i == 'K' or i == 'Q' or i == 'A':
        sums+= -1

print(sums)


cards = { 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 0, 8: 0, 9: 0, 10: -1, 'J': -1, 'K': -1, 'Q': -1,'A': -1}

sums1 = sum([cards[x] for x in current_hand])

print(sums1) 
