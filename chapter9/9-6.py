from typing import Union
from dataclasses import dataclass

# 딕셔너리 타입이 가독성이 좋은가?
my_dict: dict[str, Union[str, int]] = {
    'name': 'Tom',
    'age': 10}

@dataclass
class MyDict:
    name: str
    age: int

MyDict('hello', 10)

from typing import TypedDict
class MyDict2(TypedDict):
    name: str
    age: int

MyDict2(name='hello', age=10)

from collections import namedtuple

MyDict3 = namedtuple('MyDict3', ['name', 'age'])
a = MyDict3('hello', 10)
a.name


