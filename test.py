import pytest

from main import Category, Product


@pytest.fixture()
def cat():
    return Category('электроника', 'описание')


def test_cat(cat):
    assert cat.name == 'электроника'
    assert cat.descriptions == 'описание'

@pytest.fixture()
def prod():
    return Product('ноутбук', 'описание', 25000.00, 15)


def test_prod(prod):
    assert prod.name == 'ноутбук'
    assert prod.descriptions == 'описание'
    assert prod.price == 25000.00
    assert prod.quantity_stock == 15