from ploom import OPEN_CSV
from src.item import Item

if __name__ == '__main__':
    # Файл item.csv отсутствует.
    Item.instantiate_from_csv("Отсутствует файл item.csv")
    # FileNotFoundError: Отсутствует файл item.csv

    # В файле item.csv удалена последняя колонка.
    Item.instantiate_from_csv(OPEN_CSV)
    # InstantiateCSVError: Файл item.csv поврежден
