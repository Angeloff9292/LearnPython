import re

chickensStr = input("How many chickens?\n") 
pigsStr =input("How many pigs?\n")
cowsStr = input("How many cows?\n")

regChickens = re.match(r"^\d+$", chickensStr)
regPigs = re.match(r"^\d+$", pigsStr)
regCows = re.match(r"^\d+$", cowsStr)

if (regChickens == None or regPigs == None or regCows == None):
    print("Only positive numbers alloved")
else:
    chickensInt = int(chickensStr)
    pigsInt = int(pigsStr)
    cowsInt = int(cowsStr)

    chickensLegs = chickensInt*2
    pigsAndCowsLegs = (pigsInt + cowsInt)*4

    totalLegs = chickensLegs + pigsAndCowsLegs

    print(totalLegs)