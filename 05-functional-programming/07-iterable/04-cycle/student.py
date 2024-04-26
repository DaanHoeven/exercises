class Cycle:
    def __init__(self, list):
        self.__list = list
        self.__index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.__index = (self.__index + 1) % len(self.__list)
        return self.__list[self.__index]
