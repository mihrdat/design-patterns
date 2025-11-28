from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def price_changed(self):
        pass


class Observable:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.price_changed()


class Product(Observable):
    def __init__(self, name, unit_price):
        super().__init__()
        self._name = name
        self._unit_price = unit_price

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def unit_price(self):
        return self._unit_price

    @unit_price.setter
    def unit_price(self, value):
        self._unit_price = value
        self.notify_observers()


class StatusBar(Observer):
    def __init__(self):
        self._products = []

    def add_product(self, product):
        self._products.append(product)
        product.add_observer(self)

    def show(self):
        print("Status Bar...")
        for product in self._products:
            print(product.name)

    def price_changed(self):
        print("Price Changed - Refreshing StatusBar")
        self.show()


class Stock(Observer):
    def __init__(self):
        self._products = []

    def add_product(self, product):
        self._products.append(product)
        product.add_observer(self)

    def show(self):
        print("Stock List View...")
        for product in self._products:
            print(product.name)

    def price_changed(self):
        print("Price Changed - Refreshing StockListView")
        self.show()


status_bar = StatusBar()
stock = Stock()

product1 = Product("Pencil", 1)
product2 = Product("Book", 4)
product3 = Product("Shirt", 3)

status_bar.add_product(product1)
status_bar.add_product(product2)

stock.add_product(product1)
stock.add_product(product2)
stock.add_product(product3)

product2.unit_price = 3
product3.unit_price = 2.5
