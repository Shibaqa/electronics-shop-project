from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def __add__(self, other) -> int:
        if isinstance(other, Phone):
            return self.quantity + other.quantity
        return NotImplemented

    def __repr__(self) -> str:
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"
