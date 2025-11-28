# class CompressorType:
#     JPEG = "JPEG"
#     PNG = "PNG"


# class FilterType:
#     BLACK_AND_WHITE = "BLACK_AND_WHITE"
#     HIGH_CONTRAST = "HIGH_CONTRAST"


# class ImageStorage:
#     def __init__(self, compressor, filter):
#         self.compressor = compressor
#         self.filter = filter

#     def store(self, file_name):
#         if self.compressor == CompressorType.JPEG:
#             print(f"Compressing using JPEG")
#         elif self.compressor == CompressorType.PNG:
#             print(f"Compressing using PNG")

#         if self.filter == FilterType.BLACK_AND_WHITE:
#             print(f"Applying black and white filter")
#         elif self.filter == FilterType.HIGH_CONTRAST:
#             print(f"Applying high contrast filter")


from abc import ABC, abstractmethod


class Compressor(ABC):
    @abstractmethod
    def compress(self, image): ...


class Filter(ABC):
    @abstractmethod
    def apply(self, image): ...


class JPEGCompressor(Compressor):
    def compress(self, image):
        print(f"Compressing {image} using JPEG")


class PNGCompressor(Compressor):
    def compress(self, image):
        print(f"Compressing {image} using PNG")


class BlackAndWhiteFilter(Filter):
    def apply(self, image):
        print(f"Applying black and white filter to {image}")


class HighContrastFilter(Filter):
    def apply(self, image):
        print(f"Applying high contrast filter to {image}")


class ImageStorage:
    def store(self, image, compressor, filter):
        compressor.compress(image)
        filter.apply(image)


image_storage = ImageStorage()
image_storage.store("imageI", PNGCompressor(), BlackAndWhiteFilter())
image_storage.store("imageII", JPEGCompressor(), BlackAndWhiteFilter())

# We need to apply polymorphism principle of object-oriented programming. We want our ImageStorage to behave differently depending on the type of compressor and filter we use.


# ------------------------------------------------------------------------------
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
