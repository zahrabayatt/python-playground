# import ABC class and abstractmethod from abc(abstract base class) module
from abc import ABC, abstractmethod


class InvalidOperationError(Exception):
    pass


# there is a issues with this implementation, we can create a stream object and open it but stream class is an abstract concept and doesn't mean. We shouldn't be able to directly create an instance of the stream class. We should always subclass it and then create an instance of the subclass. That is the first issue. So, we only created this stream class as a base class to provide some code that we're going to reuse across different kinds of streams.

# The second issue is that both FileStream and NetworkStream have a read method. If we create a new stream later, we need to remember to name the method exactly read to keep things consistent. If we name it differently, like read_line or read_SDR, it won't match the other streams.
# Right now, there's no way to enforce a common interface for all streams—it's just a convention. It would be better to have a common contract or interface for different types of streams.

# class Stream:
#     def __init__(self):
#         self.opened = False

#     def open(self):
#         if self.opened:
#             raise InvalidOperationError("Stream is already opened.")

#         self.opened = True

#     def close(self):
#         if not self.opened:
#             raise InvalidOperationError("Stream is already closed.")

#         self.opened = False


# class FileStream(Stream):
#     def read(self):
#         print("Reading data from a file.")


# class NetworkStream(Stream):
#     def read(self):
#         print("Reading data from a network.")

# stream = Stream()
# stream.open()

# To solve these issues we can use an abstract base class:

class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already opened.")

        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed.")

        self.opened = False

    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading data from a file.")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network.")


# stream = Stream() we got erro
# stream.open()

# if we define another class that inherit from stream abstract class, it has to inherit the methods form stream class that decorate by abastractmethod otherwise it consider as abstract class:

class MemoryStream(Stream):
    def read(self):
        print("Reading data from a memory.")


ms = MemoryStream()
ms.open()
