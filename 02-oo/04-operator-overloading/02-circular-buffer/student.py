class CircularBuffer:
    def __init__(self, n):
        self.__n = n
        self.__list = []

    def add(self, item):
        self.__list.append(item)
        if len(self.__list) > self.__n:
            self.__list.remove(self.__list[0])

    def __len__(self):
        return len(self.__list)

    def __getitem__(self, index):
        return self.__list[index]
