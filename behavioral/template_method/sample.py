from abc import ABC, abstractmethod


# Abstract Class
class OrderProcessor(ABC):

    # Template Method
    def process_order(self):
        self.validate_order()
        self.process_payment()
        self.deliver_order()

        # Hook method
        if self.gift_wrap():
            print("Gift wrapping applied")

        self.send_confirmation()

    def validate_order(self):
        print("Validating order...")

    @abstractmethod
    def process_payment(self):
        pass

    @abstractmethod
    def deliver_order(self):
        pass

    # Hook method
    def gift_wrap(self):
        return False

    # Concrete method (common step)
    def send_confirmation(self):
        print("Sending confirmation email...")


# Concrete Class: Digital Order
class DigitalOrderProcessor(OrderProcessor):

    def process_payment(self):
        print("Processing online payment...")

    def deliver_order(self):
        print("Sending download link...")


# Concrete Class: Physical Order
class PhysicalOrderProcessor(OrderProcessor):

    def process_payment(self):
        print("Processing cash/credit card payment...")

    def deliver_order(self):
        print("Shipping the product...")

    def gift_wrap(self):
        return True


# --- Client Code ---
if __name__ == "__main__":
    print("Digital Order Processing:")
    digital_order = DigitalOrderProcessor()
    digital_order.process_order()

    print("\nPhysical Order Processing:")
    physical_order = PhysicalOrderProcessor()
    physical_order.process_order()
