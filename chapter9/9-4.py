from dataclasses import dataclass

@dataclass(eq=True, order=True)
class BigNumber:
    num1: int
    num2: int


n1 = BigNumber(10, 1)
n2 = BigNumber(9, 1)
print(n1 > n2)

