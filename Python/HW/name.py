class Name:

    def __init__(self, first_name, last_name):
        self.first_name = first_name.capitalize()
        self.last_name = last_name.capitalize()
        self.full_name = self.first_name + " " + self.last_name
        self.initials = self.first_name[0] + "." + self.last_name[0]

    # def first_name(self):
    #     return self.name.capitalize()
    #
    # def last_name(self):
    #     return self.surname.capitalize()
    #
    # def full_name(self):
    #     return self.name.capitalize() + " " + self.surname.capitalize()
    #
    # def initials(self):
    #     name = self.name.capitalize()
    #     lastName = self.surname.capitalize()
    #     fullName = name[0] +  "." + lastName[0]
    #     return fullName


n = Name("john", "smith")

print(n.first_name)
print(n.last_name)
print(n.full_name)
print(n.initials)