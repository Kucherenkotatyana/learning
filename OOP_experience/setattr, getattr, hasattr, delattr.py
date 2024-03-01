

class Person:
    CITY = "Dnipro"
    EYES = "green"
    CAR = None

    def __init__(self, name):
        self.name = name

    def change_color(self, color):
        self.EYES = color

    @classmethod
    def set_city(cls, new_city):
        cls.CITY = new_city

    def __getattribute__(self, item):
        if item == "CAR":
            raise ValueError("You can't access attribute 'CAR' via instance.")
        else:
            print(f"{self} called method __getattribute__ for {item} attribute.")
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == "x":
            raise ValueError("Invalid attribute name!")
        else:
            print(f"{self} sets value '{value}' for key '{key}'.")
            # object.__setattr__(self, key, value)
            self.__dict__[key] = value

    def __getattr__(self, item):
        print(f"{self.__dict__['name']} doesn't have {item} attribute!")
        return False

    def __delattr__(self, item):
        print(f"{self.name} deleted {item}.")
        object.__delattr__(self, item)


tanya = Person("Tanya")
# <__main__.Person object at 0x7f33973ff650> sets value 'Tanya' for key 'name'.
# <__main__.Person object at 0x7f33973ff650> called method __getattribute__ for __dict__ attribute.

olena = Person("Olena")
# <__main__.Person object at 0x7f33973ff920> called method __getattribute__ for __dict__ attribute.
# <__main__.Person object at 0x7f33973ff650> called method __getattribute__ for EYES attribute.

delattr(olena, "name")
# Olena deleted name.
