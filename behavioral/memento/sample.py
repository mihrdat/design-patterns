# Momento
class EditorSnapshot:
    def __init__(self, content):
        self.__content = content

    @property
    def content(self):
        return self.__content


# Originator
class Editor:
    def __init__(self):
        self.__content = ""

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, content):
        self.__content = content

    def create_snapshot(self):
        return EditorSnapshot(self.__content)

    def restore(self, snapshot):
        self.__content = snapshot.content


# Caretaker
class History:
    def __init__(self):
        self.__snapshots = []

    def push(self, snapshot):
        self.__snapshots.append(snapshot)

    def pop(self):
        return self.__snapshots.pop()


editor = Editor()
history = History()

editor.content = "Hello"
history.push(editor.create_snapshot())

editor.content = "Hello World!"
history.push(editor.create_snapshot())

editor.content = "ABC"

print(editor.content)

editor.restore(history.pop())

print(editor.content)
