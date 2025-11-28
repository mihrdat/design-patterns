from abc import ABC, abstractmethod


# Base command interface: defines the execute contract for all commands.
class Command(ABC):
    @abstractmethod
    def execute(self): ...


# Button holds a Command and triggers it when clicked (invoker in Command pattern).
class Button:
    def __init__(self, command):
        self.__command = command

    def click(self):
        self.__command.execute()


# Service class that performs operations related to customers (receiver in Command pattern).
class CustomerService:
    def add_customer(self):
        print("Add Customer")

    def delete_customer(self):
        print("Delete Customer")


# Concrete command that adds a customer by delegating to CustomerService.
class AddCustomerCommand(Command):
    def __init__(self, service):
        self.__service = service

    def execute(self):
        self.__service.add_customer()


# Concrete command that deletes a customer by delegating to CustomerService.
class DeleteCustomerCommand(Command):
    def __init__(self, service):
        self.__service = service

    def execute(self):
        self.__service.delete_customer()


service = CustomerService()
command = AddCustomerCommand(service)
button = Button(command)
button.click()


# -------------------------------------------------------------------------
from abc import ABC, abstractmethod


# Interface / Abstract
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


# Interface / Abstract
class UndoableCommand(Command):
    @abstractmethod
    def unexecute(self):
        pass


# Receiver
class HtmlDocument:
    def __init__(self):
        self.__content = ""

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, value):
        self.__content = value

    def make_bold(self):
        self.__content = "<b>" + self.__content + "</b>"


class History:
    def __init__(self):
        self.__commands = []

    def push(self, command):
        self.__commands.append(command)

    def pop(self):
        return self.__commands.pop()


# Concrete Command
class BoldCommand(UndoableCommand):
    def __init__(self, document, history):
        self.__previous_content = None
        self.__document = document
        self.__history = history

    def execute(self):
        self.__previous_content = self.__document.content
        self.__document.make_bold()
        self.__history.push(self)

    def unexecute(self):
        self.__document.content = self.__previous_content


# Concrete Command
class UndoCommand(Command):
    def __init__(self, history):
        self.__history = history

    def execute(self):
        self.__history.pop().unexecute()


# Invoker
class Button:
    def __init__(self, command):
        self.__command = command

    def click(self):
        self.__command.execute()


document = HtmlDocument()
history = History()

document.content = "Hello World"
print(document.content)

bold_command = BoldCommand(document, history)
bold_button = Button(bold_command)
bold_button.click()
print(document.content)


undo_command = UndoCommand(history)
undo_button = Button(undo_command)
undo_button.click()
print(document.content)
