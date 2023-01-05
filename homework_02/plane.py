"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.cargo = 0
        self.max_cargo = max_cargo

    def load_cargo(self, new_cargo):
        if self.max_cargo >= self.cargo + new_cargo:
            self.cargo += new_cargo
        else:
            raise CargoOverload("Перегрузка")

    def remove_all_cargo(self):
        before_remove = self.cargo
        self.cargo = 0
        return before_remove
