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
