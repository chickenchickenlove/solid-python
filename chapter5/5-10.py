import collections.abc

# 내장 자료형의 내부 메서드를 오버라이딩 해야하는 경우라면, collections.abc를 상속받아야 함.
# 대부분의 내장 자료형은 성능을 위해 인라인 함수로 코딩되어있어, 하나의 내장 메서드를 오버라이딩 한다고 다른 기능들이 원하는 형태로 동작하지 않을 수 있기 때문임.

def get_aliases(text):
    if text == 'rocket':
        return ['arugula']


class AliasedIngredients(collections.abc.Set):
    def __init__(self, ingredients: set[str]):
        self.ingredients = ingredients

    def __contains__(self, value: str):
        return value in self.ingredients or any(alias in self.ingredients for alias in get_aliases(value))

    def __iter__(self):
        return iter(self.ingredients)

    def __len__(self):
        return len(self.ingredients)


ingredients = AliasedIngredients({'arugula', 'eggplant', 'pepper'})
for ingredient in ingredients:
    print(ingredient)


assert ingredients == {'arugula', 'eggplant', 'pepper'}

assert len(ingredients) == 3

assert 'arugula' in ingredients
assert 'rocket' in ingredients









