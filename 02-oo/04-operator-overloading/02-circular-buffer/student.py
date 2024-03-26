class CircularBuffer:
    def __init__(self, max):
        self.__max = max
        self.__items = []

    def add(self, item):
        self.__items.append(item)
        if len(self.__items) > self.__max:
            del self.__items[0]

    def __len__(self):
        return len(self.__items)
    
    def __getitem__(self, index):
        return self.__items[index]


