

class Road:

    def __init__(self, length):
        self.length = length

    def __len__(self):
        return self.length

    def __str__(self):
        return f"Length of the road: {self.length}"

    def __del__(self):
        return "The road has been destroyed"


r = Road(100)
print(len(r))    # 100
print(r)    # Length of the road: 100
print(r.__del__())    # The road has been destroyed
