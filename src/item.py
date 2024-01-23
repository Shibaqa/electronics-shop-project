import csv
from pathlib import Path


class InstantiateCSVError(Exception):
    def __init__(self, message="Файл item.csv поврежден"):
        self.message = message
        super().__init__(self.message)


class Item:
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name[:10]

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate
        return self.price

    @classmethod
    def instantiate_from_csv(cls) -> None:
        """
        Создает экземпляры класса Item из данных в файле items.csv.
        """
        cls.all.clear()
        file_path = Path(__file__).parent.joinpath("items.csv")
        try:
            with open(file_path, 'r', encoding='windows-1251') as file:
                reader = csv.DictReader(file)
                data = list(reader)
                if 'name' not in data or 'price' not in data or 'quantity' not in data:
                    raise csv.Error('Файл item.csv поврежден')
                for row in data:
                    name = row['name']
                    price = cls.string_to_number(row['price'])
                    quantity = int(row['quantity'])
                    cls(name, price, quantity)
        except FileNotFoundError:
            raise csv.Error('Файл item.csv поврежден')

    @staticmethod
    def string_to_number(string):
        return int(float(string))

    def __repr__(self):
        return f"{__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.name

    def __add__(self, other) -> int:
        if isinstance(other, Item):
            return self.quantity + other.quantity
        return NotImplemented
