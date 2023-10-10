from dataclasses import dataclass

@dataclass
class InventoryItem:
    name: str
    unit_price: float
    quantity_on_hand: int = 0

# None을 만들어 주지는 않고, 필요한 값을 반드시 넣도록 강제한다.
A = InventoryItem('a', 0)
B = InventoryItem()