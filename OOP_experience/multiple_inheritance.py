

class Animal:

    def set_health(self, health):
        self.health = health
        print("set in animal")


class Carnivore(Animal):

    def set_health(self, health):
        self.health = health
        print("set in carnivore")


class Mammal(Animal):

    def set_health(self, health):
        self.health = health
        print("set in mammal")


class Dog(Mammal, Carnivore):

    def set_health(self, health):
        Mammal.set_health(self, health)
        Carnivore.set_health(self, health)
        Animal.set_health(self, health)

        print("set in dog")


dog = Dog()
dog.set_health(10)
# set in mammal
# set in carnivore
# set in animal
# set in dog


# ---- multiple inheritance with super() (MRO) ----


class Animal:

    def set_health(self, health):
        self.health = health
        print("set in animal")


class Carnivore(Animal):

    def set_health(self, health):
        self.health = health
        super().set_health(health)
        print("set in carnivore")


class Mammal(Animal):

    def set_health(self, health):
        self.health = health
        super().set_health(health)
        print("set in mammal")


class Dog(Mammal, Carnivore):

    def set_health(self, health):
        super().set_health(health)

        print("set in dog")


dog = Dog()
dog.set_health(10)
# set in animal
# set in carnivore
# set in mammal
# set in dog


class Animal:

    def __init__(self):
        self.health = 100

    def hit(self, damage):
        self.health -= damage


class Carnivore(Animal):

    def __init__(self):
        super().__init__()
        self.legs = 4


carn = Carnivore()
carn.hit(10)
print(carn.health)    # 90
