from abc import ABC, abstractmethod


#Good example for inheritance

class Invalid(Exception):
    pass


class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise Invalid("Steam is already on Process")

        self.opened = True

    def close(self):
        if not self.opened:
            raise Invalid("Steam is already on process")

        self.opened = False
    @abstractmethod
    def read(self):
        pass
class FileStream(Stream):
    def read(self):
        print("reading data from the file")

class NetworkStream(Stream):
    def read(self):
        print("reading data from the Network")

class MemorySteam(Stream):
    def read(self):
        print("Reading data from a memory steam.")



#Execution

Stream =MemorySteam()

Stream.open()
