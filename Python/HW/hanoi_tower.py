def solve_hanoi_tower(discs):
    if discs == 0:
        return 0
    elif discs == 1:
        return 1
    else:
        discs = solve_hanoi_tower(discs - 1)
        return discs*2+1

print(solve_hanoi_tower(4))