from abc import ABC, abstractmethod


# Interface
class Iterator(ABC):
    @abstractmethod
    def has_next(self): ...

    @abstractmethod
    def current(self): ...

    @abstractmethod
    def next(self): ...


class BrowseHistory:
    def __init__(self):
        self.__urls = []

    @property
    def urls(self):
        return self.__urls

    # class __StackIterator(Iterator): ...
    # class __AnotherDataStructureIterator(Iterator): ...

    class __ListIterator(Iterator):
        def __init__(self, history):
            self.__history = history
            self.__index = 0

        def has_next(self):
            return self.__index < len(self.__history.urls)

        def current(self):
            return self.__history.urls[self.__index]

        def next(self):
            self.__index += 1

    def push(self, url):
        self.__urls.append(url)

    def pop(self):
        return self.__urls.pop()

    # def get_urls(self):
    #     return self.urls

    def create_iterator(self):
        return self.__ListIterator(self)


# history = BrowseHistory()
# history.push("a")
# history.push("b")
# history.push("c")

# for url in history.get_urls():
#     print(url)


history = BrowseHistory()
history.push("a")
history.push("b")
history.push("c")

iterator = history.create_iterator()

while iterator.has_next():
    url = iterator.current()
    print(url)
    iterator.next()
