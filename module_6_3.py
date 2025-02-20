import random

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed, cords):
        self.cords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        if self.cords[2] + dz * self.speed < 0:
            print("It's too deep, I can't dive :(")
        else:
            self.cords[0] += dx * self.speed
            self.cords[1] += dy * self.speed
            self.cords[2] += dz * self.speed

    def get_cords(self):
        print(f'X: {self.cords[0]}, Y: {self.cords[1]}, Z: {self.cords[2]}')

    def attack(self):
        if Animal._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        if Animal._DEGREE_OF_DANGER >= 5:
            print("Be careful, i'm attacking you 0_0" )


class Bird(Animal):
    beak = True

    def lay_eggs(self):
        print(f'"Here are(is) {random.randint(1,4)} eggs for you"')

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        self.cords[2] -= abs(dz) * (self.speed // 2)

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(Bird, AquaticAnimal, PoisonousAnimal, ):
    SOUND = "Click-click-click"
    def speak(self, SOUND):
        print(self.SOUND)

db = Duckbill(10,[0,0,0])

print(db.live)
print(db.beak)

db.speak(Duckbill.SOUND)
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()