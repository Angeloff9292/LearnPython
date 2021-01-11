# class Animal:
#     def die(self):
#         print('bye-bye')
#         self.healt = 0
#
# class Carnivor:
#     def hant(self):
#         print('eating')
#         self.satity = 100
#
# class Dog (Animal, Carnivor):
#     def bark(self):
#         print('woof woof')
#
# dog = Dog()
# dog.bark()
# dog.hant()
# dog.die()
#
# class Animal:
#     def set_health(self, health):
#         print('Set in animal')
#
# class Carnivor(Animal):
#     def set_health(self, health):
#         Animal.set_health(self, health)
#         print('Set in carnivor')
#
# class Mammal(Animal):
#     def set_health(self, health):
#         Animal.set_health(self, health)
#         print('Set in mamal')
#
# class Dog(Mammal, Carnivor):
#     def set_health(self, health):
#         Mammal.set_health(self, health)
#         Carnivor.set_health(self, health)
#
#         print('Set in dog')
# dog = Dog()
# dog.set_health(10)

class Animal:
    def __init__(self):
        self.health = 100

    def hit(self, damage):
        self.health -= damage

class Carnivor(Animal):

    def __init__(self):
        super().__init__()
        self.legs = 4
c = Carnivor()
c.hit(10)

print(c.health)