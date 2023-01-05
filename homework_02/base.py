from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    weight = 2000
    started = False
    fuel = 60
    fuel_consumption = 12

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError("Топливо на нуле!")
        #return self.started  скорее всего что-то лишнее, без него так же работает

    def move(self, distance):
        distance_cost = self.fuel_consumption * distance
        if self.fuel >= distance_cost:
            self.fuel -= distance_cost
        else:
            raise NotEnoughFuel("Топлива не достаточно для преодоления данной дистанции")


