from dataclasses import dataclass

@dataclass(eq=True)
class MyData:
    name: str

@dataclass(eq=False)
class MyDataNotEq:
    name: str

print(MyData('a') == MyData('a'))
print(MyDataNotEq('a') == MyDataNotEq('a'))




