import csv

import pytest

from src.item import Item


@pytest.fixture
def item_1():
    return Item("Смартфон", 10000, 20)


def test_calculate_total_price(item_1):
    assert item_1.calculate_total_price() == 200000


def test_apply_discount(item_1):
    assert item_1.apply_discount() * 0.8 == 8000.0


def test_instantiate_from_csv():
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
        with open("ite.csv", encoding="windows-1251") as csvfile:
            items = csv.DictReader(csvfile, delimiter=",")


def test_instantiate_from_csv_corrupted_file():
    with pytest.raises(csv.Error):
        Item.instantiate_from_csv()
