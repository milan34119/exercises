class Queue:
    def __init__(self):
        self.__queue = []
    
    def add(self, item):
        self.__queue.append(item)
        
    def next(self):
        if not self.is_empty():
            return self.__queue.pop(0)
        else:
            print('nu-uh')
            
    def is_empty(self):
        return len(self.__queue) == 0