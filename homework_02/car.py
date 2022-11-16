"""
создайте класс `Car`, наследник `Vehicle`
"""
from dataclasses import dataclass

from homework_02.base import Vehicle
from homework_02.engine import Engine


@dataclass(Engine)
class Car(Vehicle):
    engine = None
