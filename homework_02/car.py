"""
создайте класс `Car`, наследник `Vehicle`
"""
from dataclasses import dataclass

from homework_02.base import Vehicle
from homework_02.engine import Engine


@dataclass()
class Car(Vehicle):
    engine = Engine(volume=None, pistons=None)

    def __init__(self, ):
        super().__init__(weight=0, fuel=0, fuel_consumption=0)

    def set_engine(self, engine):
        engine.__init__(self, volume, pistons)
