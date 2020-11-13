def square(*args):
    return[x*x for x in args]

result = square(1, 2, 3, 4, 5)

print(result)

def triple(*args):
    return[x*3 for x in args]

result = triple(1, 2, 3, 4, 5)

print(result)

def square1(number):
    return number*number

numbers = [1, 2, 3, 4, 5]

mapped_seq = map(square1, numbers)

for x in mapped_seq:
    print(x)

def is_adult(age):
    return age>=18

ages = [14, 13, 18, 22, 24]

print(list(filter(is_adult, ages)))

is_adult = lambda age: age>=18

print(list(filter(lambda age: age>=18, ages)))