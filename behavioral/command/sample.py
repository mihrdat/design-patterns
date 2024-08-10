from abc import ABC, abstractmethod


# Framework code --------------------------------------
class Command(ABC):
    @abstractmethod
    def execute(self): ...


class Button:
    def __init__(self, command):
        self.__command = command

    def click(self):
        self.__command.execute()


# -----------------------------------------------------


# Application code ------------------------------------
class CustomerService:
    def add_customer(self):
        print("Add Customer")

    def delete_customer(self):
        print("Delete Customer")


class AddCustomerCommand(Command):
    def __init__(self, service):
        self.__service = service

    def execute(self):
        self.__service.add_customer()


class DeleteCustomerCommand(Command):
    def __init__(self, service):
        self.__service = service

    def execute(self):
        self.__service.delete_customer()


# -----------------------------------------------------


service = CustomerService()
command = AddCustomerCommand(service)
button = Button(command)
button.click()
