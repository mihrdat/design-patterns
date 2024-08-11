from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, value): ...


class SpreadSheet(Observer):
    def update(self, value):
        print(f"SpreadSheet got notified: {value}")


class Chart(Observer):
    def update(self, value):
        print(f"Chart got notified: {value}")


# Observable
class Subject:
    def __init__(self):
        self.__observers = []

    def register(self, observer):
        self.__observers.append(observer)

    def unregister(self, observer):
        self.__observers.remove(observer)

    def notify(self, value):
        for observer in self.__observers:
            observer.update(value)


class DataSource(Subject):
    def __init__(self):
        super().__init__()
        self.__value = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value
        self.notify(self.__value)


data_source = DataSource()
spread_sheet1 = SpreadSheet()
spread_sheet2 = SpreadSheet()
chart = Chart()

data_source.register(spread_sheet1)
data_source.register(spread_sheet2)
data_source.register(chart)

data_source.value = 10
