from abc import ABC, abstractmethod


class Handler(ABC):
    def __init__(self, next):
        self.__next = next

    @abstractmethod
    def handle(self, request):
        pass

    def call_next(self, request):
        if self.__next:
            self.__next.handle(request)


class Authenticator(Handler):
    def handle(self, request):
        print("Authentication")
        is_valid = (request.username == "john") and (request.password == "12345")

        # stop processing on invalid credentials
        if not is_valid:
            return

        # continue chain
        self.call_next(request)


class Compressor(Handler):
    def handle(self, request):
        print("Compress")
        # always continue
        self.call_next(request)


class Logger(Handler):
    def handle(self, request):
        print("Log")
        # always continue
        self.call_next(request)


class HttpRequest:
    def __init__(self, username, password):
        self._username = username
        self._password = password

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password


class Webserver:
    def __init__(self, handler):
        self._handler = handler

    def handle(self, request):
        self._handler.handle(request)


compressor = Compressor(None)
logger = Logger(compressor)
authenticator = Authenticator(logger)

web_server = Webserver(authenticator)
request = HttpRequest("john", "12345")
web_server.handle(request)
