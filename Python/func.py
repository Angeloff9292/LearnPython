def variable():
    name = "John" #string
    sallary = 999 #int
    isMarried = True #boolean

    print("Hello ", name, "!")
    print("My amount is" , sallary)
    print("Im married?", isMarried)

variable() 

config = {
    "browser": "chrome",
    "test": "smoke",
    "cycles": 100,
    "log": True
}

def getDictionaryValue(key):
    return config.get(key)

print(getDictionaryValue("test"))