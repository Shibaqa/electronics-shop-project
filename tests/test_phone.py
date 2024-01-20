import pytest

from src.item import Item
from src.phone import Phone
from tests.test_item import item_1



@pytest.fixture
def phone1(request):
    phone = Phone("Тестовый смартфон 1", 500.0, 3, 2)

    def finalize():
        if phone in Phone.all:
            Phone.all.remove(phone)

    request.addfinalizer(finalize)
    return phone

    def finalize():
        if phone in Phone.all:
            Phone.all.remove(phone)

    request.addfinalizer(finalize)
    return phone


def test_phone_inherits_from_item(phone1):
    assert isinstance(phone1, Phone)
    assert isinstance(phone1, Item)


def test_number_of_sim(phone1):
    assert phone1.number_of_sim == 2


def test_phone_addition(phone1, item_1):
    with pytest.raises(TypeError, match="unsupported operand type\(s\) for \+: 'Phone' and 'Item'"):
        result = phone1 + item_1
