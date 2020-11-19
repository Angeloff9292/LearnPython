def calc_dice_scores(lst):
    return sum([a+b for a, b in lst]) if not any([a==b for a, b in lst]) else 0

    
n = [(1, 1), (2, 3), (4, 5)]

print(calc_dice_scores(n))