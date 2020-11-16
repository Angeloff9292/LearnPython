def calc_dice_scores(lst):
    count = 0
    for a, b in lst:
        if a!=b:
            ret = a+b
            count += ret
        else:
            count = 0
    return count


    
n = [(1, 1), (2, 3), (4, 5)]

print(calc_dice_scores(n))