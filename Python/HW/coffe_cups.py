alredyCupsStr = input("How many cups you already drink?\n")
reg = re.match(r"^\d+$", alredyCupsStr)

result=reg==None


if (result == True):
    print("Pls, enter only positive numbers!")    
else:
    alredyCups = int(alredyCupsStr)
    bonusCups = int(alredyCups/6)

    print(bonusCups)