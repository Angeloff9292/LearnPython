greatting = "Hello from the global scope"

def greet():
    greatting = "Enclosing"

    def nested():
        greatting = "Local"
        print(greatting)
    nested()

print(greet())
print(greatting)

def greet(greatting):
    print