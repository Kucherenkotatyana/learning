

class Character:

    MAX_SPEED = 100

    def __init__(self, race, damage=10):
        self.__race = race
        self._health = 100
        self.damage = damage

        self._current_speed = 20

    def hit(self, damage):
        self._health -= damage

    @property
    def health(self):
        return self._health

    @property
    def race(self):
        return self.__race

    @property
    def current_speed(self):
        return self._current_speed

    @current_speed.setter
    # protection from invalid data
    def current_speed(self, current_speed):
        if current_speed < 0:
            self._current_speed = 0
        elif current_speed > 100:
            self._current_speed = 100
        else:
            self._current_speed = current_speed


c = Character('Elf')
# print(c.__race)    # AttributeError: 'Character' object has no attribute '__race'


c.current_speed = 1000
print(c.current_speed)    # 100
