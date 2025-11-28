from abc import ABC, abstractmethod


class Mediator(ABC):
    @abstractmethod
    def notify(self, sender, event):
        pass


class UIComponent:
    def __init__(self, mediator=None):
        self.__mediator = mediator


class TextBox(UIComponent):
    def __init__(self, name, mediator=None):
        super().__init__(mediator)
        self.__name = name
        self.__content = ""

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, value):
        self.__content = value
        if self.__mediator:
            self.__mediator.notify(self, "content_changed")

    def is_filled(self):
        return len(self.__content.strip()) > 0


class CheckBox(UIComponent):
    def __init__(self, mediator=None):
        super().__init__(mediator)
        self.__is_checked = False

    @property
    def is_checked(self):
        return self.__is_checked

    @is_checked.setter
    def is_checked(self, value):
        self.__is_checked = value
        if self.__mediator:
            self.__mediator.notify(self, "checkbox_changed")


class Button(UIComponent):
    def __init__(self, mediator=None):
        super().__init__(mediator)
        self.__is_enable = False

    @property
    def is_enabled(self):
        return self.__is_enable

    @is_enabled.setter
    def is_enabled(self, value):
        self.__is_enable = value

    def click(self):
        if self.__is_enable and self.__mediator:
            self.__mediator.notify(self, "button_clicked")


class SignUpDialogBox(Mediator):
    def __init__(self):
        # Create UI components
        self.username = TextBox("username", self)
        self.password = TextBox("password", self)
        self.terms_of_service = CheckBox(self)
        self.sign_up_button = Button(self)

        # Initial state
        self.__update_button_state()

    def notify(self, sender, event):
        """Mediator pattern - handle component interactions"""
        if event in ["content_changed", "check_changed"]:
            self.__update_button_state()
        elif event == "button_clicked":
            self.__handle_signup()

    def __update_button_state(self):
        """Update button enabled state based on form validation"""
        is_username_filled = self.username.is_filled()
        is_password_filled = self.password.is_filled()
        is_terms_agreed = self.terms_of_service.is_checked()

        self.sign_up_button.is_enabled = (
            is_username_filled and is_password_filled and is_terms_agreed
        )

    def __handle_signup(self):
        """Handle the signup process"""
        print(f"Signing up user: {self.username.content}")
        print("Sign up successful!")


# Example usage
if __name__ == "__main__":
    # Create the dialog box
    dialog = SignUpDialogBox()

    # Simulate user interactions
    print("=== Initial state ===")

    print("\n=== User enters username ===")
    dialog.username.content = "john_doe"

    print("\n=== User enters password ===")
    dialog.password.content = "secret123"

    print("\n=== User checks terms agreement ===")
    dialog.terms_of_service.__is_checked = True

    print("\n=== User clicks sign up button ===")
    dialog.sign_up_button.click()

    print("\n=== User unchecks terms ===")
    dialog.terms_of_service.__is_checked = False

    print("\n=== User tries to click disabled button ===")
    dialog.sign_up_button.click()  # Should not process since button is disabled
