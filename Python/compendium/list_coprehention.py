# greeting = input('Enter any info: \n')
# chars = []

# for l in greeting:
#     chars.append(l)

# chars.reverse()

# string = "".join(chars)

# print(string)

chars = [l for l in range(0, 11)]

print(chars)

list1 = [2, -2, 5, 8, 11, 3]
list2 = [-2, 2, -5, 8, 13, -3]

# Возможность создавать списки с упрощенным синтаксисом.
pairs = [(x, y) for x in list1 for y in list2 if x+y==0]
print(pairs)