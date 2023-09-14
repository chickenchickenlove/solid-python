from enum import Enum
from typing import List


class Animal(Enum):

    DOG = ('Dog', lambda: print('bark'))
    CAT = ('Cat', lambda: print('meow'))
    PIG = ('Pig', lambda: print('Ggul'))

    def __new__(cls, name, func):
        obj = object.__new__(cls)
        obj._value_ = name
        obj.action = func
        return obj

    def action(self):
        self.action()

    def __str__(self):
        return self.value


for a in Animal:
    a.action()

def do_function(my_list: List[Animal]):
    for m in my_list:
        m.action()
