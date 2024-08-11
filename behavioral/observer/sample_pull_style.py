from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self): ...


class SpreadSheet(Observer):
    def __init__(self, data_source):
        self.__data_source = data_source

    def update(self):
        print(f"SpreadSheet got notified: {self.__data_source.value}")


class Chart(Observer):
    def __init__(self, data_source):
        self.__data_source = data_source

    def update(self):
        print(f"Chart got notified: {self.__data_source.value}")


# Observable
class Subject:
    def __init__(self):
        self.__observers = []

    def register(self, observer):
        self.__observers.append(observer)

    def unregister(self, observer):
        self.__observers.remove(observer)

    def notify(self):
        for observer in self.__observers:
            observer.update()


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
        self.notify()


data_source = DataSource()
spread_sheet1 = SpreadSheet(data_source)
spread_sheet2 = SpreadSheet(data_source)
chart = Chart(data_source)

data_source.register(spread_sheet1)
data_source.register(spread_sheet2)
data_source.register(chart)

data_source.value = 10
