wand = 10

def data_analysis(numbers):
    global wand
    if numbers > 3 or numbers < 0:
        print("Error, try again")
        # continue
    else:
        wand -= numbers
        print(wand)
    if wand == 0 or wand < 0:
        print("You lose")
    


while wand > 0:
    p1 = int(input(f"P1 Enter number from 1 to 3:"))
    data_analysis(p1)

    p2 = int(input(f"P2 Enter number from 1 to 3:"))
    data_analysis(p2)