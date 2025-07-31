from abc import ABC, abstractmethod


class Handler(ABC):
    def __init__(self, next):
        self._next = next

    @abstractmethod
    def do_handle(self, request): ...

    def handle(self, request):
        if self.do_handle(request):
            return

        if self._next:
            self._next.handle(request)


class Authenticator(Handler):
    def __init__(self, next):
        super().__init__(next)

    def do_handle(self, request):
        print("Authentication")
        is_valid = (request.username == "john") and (request.password == "12345")

        return not is_valid


class Compressor(Handler):
    def __init__(self, next):
        super().__init__(next)

    def do_handle(self, request):
        print("Compress")

        # we're returning false, which means we're not done processing or handling the request.
        # and that means the next handler in the chain should be called.
        return False


class Logger(Handler):
    def __init__(self, next):
        super().__init__(next)

    def do_handle(self, request):
        print("Log")

        return False


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
web_server.handle(HttpRequest("john", "12345"))
