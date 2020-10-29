def greeting():
    '''
    DOCSTRING:info about functiona
    INPUT: no input
    OUTPUT: Hello!
    '''
    print("Hello")

greeting()

# help(greeting)

def print_name(name):
    print(name)

print_name("Elaija")

def print_name(name = "Default"):
    print(name)

print_name()

result = print_name()
print(result)
print(type(result))

def get_greeting(name):
    return 'Hello ' + name
greeting = get_greeting('Oleg')
print(greeting)

def get_sum(a, b):
    return a+b
result = get_sum(10, 2)

print_name(result)

def is_adult(age):
    return age >= 18

result = is_adult(18)
print(result)

def is_palindrome(text):
    return text == text[::-1]

result = is_palindrome("sos")
print(result)

def calc_taxes(p1, p2, p3):
    return sum((p1, p2, p3)) * 0.06

print(round(calc_taxes(10, 20, 30), 2))

def calc_taxes(*args):
    return sum(args) * 0.06

print(round(calc_taxes(10,20,30,40,50), 2))

def save_players(**kwargs):
    for k,v in kwargs.items():
        print(f'Player {k} has rating {v}')
save_players(Carlsen=2800, Giri=2780)