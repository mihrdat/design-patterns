from abc import ABC, abstractmethod


class UIControl:
    def __init__(self, owner):
        self._owner = owner


class DialogBox(ABC):
    @abstractmethod
    def changed(self, control): ...


class ListBox(UIControl):
    def __init__(self, owner):
        super().__init__(owner)
        self._selection = None

    @property
    def selection(self):
        return self._selection

    @selection.setter
    def selection(self, value):
        self._selection = value
        self._owner.changed(self)


class TextBox(UIControl):
    def __init__(self, owner):
        super().__init__(owner)
        self._content = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
        self._owner.changed(self)


class Button(UIControl):
    def __init__(self, owner):
        super().__init__(owner)
        self._is_enabled = None

    @property
    def is_enabled(self):
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, value):
        self._is_enabled = value
        self._owner.changed(self)


class ArticlesDialogBox(DialogBox):
    def __init__(self):
        self._articles_list_box = ListBox(self)
        self._title_text_box = TextBox(self)
        self._save_button = Button(self)

    def changed(self, control):
        if control == self._articles_list_box:
            self.__article_selected()
        elif control == self._title_text_box:
            self.__title_changed()

    def simulate_user_interaction(self):
        self._articles_list_box.selection = "Article 1"
        self._title_text_box.content = ""
        print(f"Textbox: {self._title_text_box.content}")
        print(f"Button: {self._save_button.is_enabled}")

    def __title_changed(self):
        content = self._title_text_box.content
        is_empty = content is None or content == ""
        self._save_button.is_enabled = not is_empty

    def __article_selected(self):
        self._title_text_box.content = self._articles_list_box.selection
        self._save_button.is_enabled = True


dialog = ArticlesDialogBox()
dialog.simulate_user_interaction()
