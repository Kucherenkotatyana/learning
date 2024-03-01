"""
Descriptors are Python objects that implement a method of the descriptor protocol,
which gives you the ability to create objects that have special behavior when they’re
accessed as attributes of other objects.
"""


class StringField:

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, data):
        data = str(data)
        self._value = data

    @value.deleter
    def value(self):
        self._value = None


class IntegerField:

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, data):
        data = int(data)
        self._value = data

    @value.deleter
    def value(self):
        self._value = None


class Animal:

    def __init__(self, name, age):
        self._name = StringField()
        self._age = IntegerField()

        self._instance_creator(name, age)

    def _instance_creator(self, name, age):
        self._name.value = name
        self._age.value = age
