person = {'name': 'Tom', 'age': 10}
# 무슨 타입? age가 존재하긴 하나?
person.get('age')


from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int

p = Person('a', 10)
name = p.name
age = p.age


print(p)
print(str(p))
print(repr(p))




