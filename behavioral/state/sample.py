"""
class ToolType:
    SELECTION = "selection"
    BRUSH = "brush"
    ERASER = "eraser"


class Canvas:
    def __init__(self):
        self._current_tool = None

    @property
    def current_tool(self):
        return self._current_tool

    @current_tool.setter
    def current_tool(self, tool):
        self._current_tool = tool

    def mouse_down(self):
        if self.current_tool == ToolType.SELECTION:
            print("Selection icon")
        elif self.current_tool == ToolType.BRUSH:
            print("Brush icon")
        elif self.current_tool == ToolType.ERASER:
            print("Eraser icon")

    def mouse_up(self):
        if self.current_tool == ToolType.SELECTION:
            print("Draw dashed rectangle")
        elif self.current_tool == ToolType.BRUSH:
            print("Draw a line")
        elif self.current_tool == ToolType.ERASER:
            print("Erase something")


canvas = Canvas()
canvas.current_tool = ToolType.BRUSH
canvas.mouse_down()
canvas.mouse_up()

canvas.current_tool = ToolType.ERASER
canvas.mouse_down()
canvas.mouse_up()
"""


from abc import ABC, abstractmethod


# State
class Tool(ABC):
    @abstractmethod
    def mouse_down(self): ...

    @abstractmethod
    def mouse_up(self): ...


# Concrete State A
class SelectionTool(Tool):
    def mouse_down(self):
        print("Selection icon")

    def mouse_up(self):
        print("Draw dashed rectangle")


# Concrete State B
class BrushTool(Tool):
    def mouse_down(self):
        print("Brush icon")

    def mouse_up(self):
        print("Draw a line")


# Concrete State C
class EraserTool(Tool):
    def mouse_down(self):
        print("Eraser icon")

    def mouse_up(self):
        print("Erase something")


# Context
class Canvas:
    def __init__(self):
        self.__current_tool = None

    @property
    def current_tool(self):
        return self.__current_tool

    @current_tool.setter
    def current_tool(self, tool):
        self.__current_tool = tool

    def mouse_down(self):
        self.current_tool.mouse_down()

    def mouse_up(self):
        self.__current_tool.mouse_up()


canvas = Canvas()
canvas.current_tool = BrushTool()
canvas.mouse_down()
canvas.mouse_up()

canvas.current_tool = EraserTool()
canvas.mouse_down()
canvas.mouse_up()

# This is a very important principle in object-oriented programming called the Open/Closed Principle.
# The code is now open for extension and closed for modification.
