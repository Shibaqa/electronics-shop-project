from src.item import Item
from src.language_mixin import LanguageMixin


class Keyboard(LanguageMixin, Item):

    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__(name, price, quantity)
