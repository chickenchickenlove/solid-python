from dataclasses import dataclass

@dataclass(frozen=True)
class BigNumber:
    num1: int
    num2: int
    num_list: list

n1 = BigNumber(1,2, [])

# 이건 안됨. (불변 객체)
# n1.num1 = 10

# 이건 됨.
n1.num_list.append('hello')