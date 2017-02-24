#OOP

#Create an object

#There must be:
#   A constructor
#   At least 5 fields
#   At least three methods

class shoes():
    def __init__(self, color, size, material, brand, damage, shype):
        self.color = color
        self.size = size
        self.material = material
        self.durability = 100
        self.brand = brand
        self.damage = damage
        self.shype = shype
    def kick(self):
        print 'You kick your opponent with your',self.shype,'.\
         \nYou have dealt',self.damage,'damage.'
        self.durability -= 1
    def hit(self):
        print 'You take off your',self.shype,'and hit your opponent with them.\
        \nYou have dealt',self.damage,'damage.'
        self.durability -= 1
    def throw(self):
        print 'You have thrown your',self.shype,'at your opponent.\
        \nYou have dealt',self.damage,'damage.'
        self.durability -= 1
my_shoes = shoes('black', '8', 'plastic', 'Nike', '5', 'sneakers')