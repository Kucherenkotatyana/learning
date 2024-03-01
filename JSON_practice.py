"""
The JSON encoder implemented in the dump() and dumps() methods
can serialize only a few basic object types. These are
dictionaries, lists, strings, integers, floats, Booleans, and None.
"""

import json


# ----- ----- ----- case №1 ----- ----- -----
class Tournament:

    def __init__(self, name, year):
        self.name = name
        self.year = year


t1 = Tournament("Football", 2010)
t2 = Tournament("Paintball", 2013)
t3 = Tournament("Horseriding", 2012)


dumped_data = json.dumps(t1.__dict__)    # {"name": "Football", "year": 2010}
loaded_data = Tournament(**json.loads(dumped_data))    # <__main__.Tournament object at 0x7f8fc74dcf60>
print(f"name = {loaded_data.name}, year = {loaded_data.year}")    # name = Football, year = 2010


# ----- ----- ----- case №2 ----- ----- -----
class Tournament:

    def __init__(self, name, year):
        self.name = name
        self.year = year

    @classmethod
    def from_json(cls, json_data):
        return cls(**json_data)


class Player:

    def __init__(self, tournaments):
        self.tournaments = tournaments

    @classmethod
    def from_json(cls, json_data):
        tournaments = list(map(Tournament.from_json, json_data["tournaments"]))
        return cls(tournaments)


tournament1 = Tournament("football", 2018)
tournament2 = Tournament("horseriding", 2020)
tournament3 = Tournament("swimming", 2007)
player = Player([tournament1, tournament2, tournament3])

json_data = json.dumps(player, default=lambda obj: obj.__dict__)
decoded_player = Player.from_json(json.loads(json_data))

print(decoded_player)    # returns Player object
print(decoded_player.tournaments)    # returns list of Tournament objects


# ----- ----- ----- serialization and deserialization to/from JSON ----- ----- -----
with open("json_player", "w") as file:
    json.dump(player, file, default=lambda obj: obj.__dict__)

with open("json_player", "r") as read_file:
    data = json.load(read_file)
    print(data)
    # {
    #     'tournaments': [
    #         {'name': 'football', 'year': 2018},
    #         {'name': 'horseriding', 'year': 2020},
    #         {'name': 'swimming', 'year': 2007}
    #     ]
    # }
