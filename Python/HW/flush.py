table_cads = ["A_C", "J_H", "7_D", "8_C", "10_C"]
hand_cards = ["J_C", "3_C"]

total_hands = table_cads + hand_cards

new_total_hands = []
for i in total_hands:
    new_total_hands.append(i.split('_')[1])

new_total_hands_STR = str(new_total_hands)

if new_total_hands_STR.count('D') >= 5 or new_total_hands_STR.count('S') >= 5 or new_total_hands_STR.count('H') >= 5 or new_total_hands_STR.count('C') >= 5:
    print('Flush!')
else:
    print('No Flush!')