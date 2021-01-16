class Employee:

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    @classmethod
    def from_string(cls, str_to_parse):
        data = str_to_parse.split("-")
        return cls(data[0], data[1], int(data[2]))

c = Employee ("John", "Smith", 5000)
