from enum import Enum
from typing import List


class Animal(Enum):

    # Enum 클래스에 인스턴스로 생성됨.
    DOG = ('Dog', lambda: print('bark'))
    CAT = ('Cat', lambda: print('meow'))
    PIG = ('Pig', lambda: print('Ggul'))

    # 생성될 때는 생성자가 호출됨. 이 때, 필요한 값을 넣어줄 수 있음.
    def __new__(cls, name, func):
        obj = object.__new__(cls)
        obj._value_ = name # Enum은 _value_를 가지고 있음. 내부적으로 _value_는 self.value로 바꾸어짐.
        obj.action = func
        return obj

    def action(self):
        self.action()

    def get_value(self):
        return self.value #

    def __str__(self):
        return self.value


for a in Animal:
    a.action()

# typing을 이용해서 변수의 타입을 IDE에서 인식하도록 할 수 있음.
def do_function(my_list: List[Animal]):
    for m in my_list:
        m.action()
