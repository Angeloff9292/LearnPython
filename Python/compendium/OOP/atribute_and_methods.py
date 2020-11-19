class Character():
    max_speed = 100
    dead_health = 0
    def __init__(self, race, damage=10, armor=20):
        self.race = race
        self.damage = damage
        self.armor = armor
        self.heals = 100
    
    def hit(self, damage):
        self.heals -= damage

    def is_dead(self):
        return self.heals == Character.dead_health

unit = Character('Ork')

unit.hit(100)
print(unit.heals)
print(unit.is_dead())