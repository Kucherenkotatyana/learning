

class Character:

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)
        return obj

    def __init__(self):
        self.race = "Elf"


class NewCharacter:

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __del__(self):
        NewCharacter._instance = None

    def __init__(self):
        self.race = "Elf"


a = NewCharacter()    # Elf
b = NewCharacter()    # Elf

b.race = "Ork"

print(a.race)       # Ork
print(b.race)       # Ork

print(a)    # <__main__.CharacterNew object at 0x7f71a026d080>
print(b)    # <__main__.CharacterNew object at 0x7f71a026d080>
