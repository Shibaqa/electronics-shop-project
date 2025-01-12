import pytest

from ploom import OPEN_CSV
from src.item import Item, InstantiateCSVError


@pytest.fixture
def item_1():
    return Item("Смартфон", 10000, 20)


def test_calculate_total_price(item_1):
    assert item_1.calculate_total_price() == 200000


def test_apply_discount(item_1):
    assert item_1.apply_discount() * 0.8 == 8000.0


def instantiate_from_csv(cls) -> None:
    Item.instantiate_from_csv()
    assert len(Item.all) == 5


def test_string_to_number(item_1):
    assert Item.string_to_number("5") == 5
    assert Item.string_to_number("5.0") == 5
    assert Item.string_to_number("5.5") == 5


def test_repr(item_1):
    assert repr(item_1) == "Item('Смартфон', 10000, 20)"


def test_str(item_1):
    assert str(item_1) == 'Смартфон'


def test_instantiate_from_csv_file_not_found():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv("Отсутствует файл item.csv")


def test_instantiate_from_csv_corrupted_file():
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv(OPEN_CSV)
