class Category:
    name = str
    descriptions = str
    goods = list

    def __init__(self, name, description):
        self.name = name
        self.descriptions = description
        self.goods = []
        self.categories = []
        self.products = []


class Product:
    name = str
    descriptions = str
    price = float
    quantity_stock = int

    def __init__(self, name, descriptions, price, quantity_stock):
        self.name = name
        self.descriptions = descriptions
        self.price = price
        self.quantity_stock = quantity_stock


if __name__ == '__main__':
    category1 = Category('электроника', 'описание')
    prod1 = Product('ноутбук', 'описание', '25000,00', 15)

