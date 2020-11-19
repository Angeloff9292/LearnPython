def divine(a, b):
    try:
        return a/b
    except ZeroDivisionError as ex:
        print(f"An error occurated: {ex}")

divine(4, 0)

def divine1(a, b):
    try:
        return a/b
    except:
        print(f"An error occurated")

divine1(4, "blbla")

file = None
try:
    file = open(r'C:\temp\test.txt')
    data = file.read()

except:
    print("Error occurate")

finally:
    print ('Finnaly')
    if file != None:
        file.close()

def get_int():
    while True:
        try:
            reply = int(input("Enter a phone number:"))
            return reply
        except:
            print('Not a number, try again.')
            continue

print(get_int())