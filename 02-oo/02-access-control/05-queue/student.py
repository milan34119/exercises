# class Queue:
#     def __init__(self):
#         self.__queue = []
    
#     def add(self, item):
#         self.__queue.append(item)
        
#     def next(self):
#         if not self.is_empty():
#             return self.__queue.pop(0)
#         else:
#             print('nu-uh')
            
#     def is_empty(self):
#         return len(self.__queue) == 0





















# * Create a class `Queue`.
# * Its constructor takes no parameters.
#   A new queue is initially empty.
# * Add a method `add(self, item)` to add an item to the queue.
# * Add a method `next(self)` that removes and returns the next item from the queue.
# * Add a method `is_empty(self)` that checks if the queue is empty.

class Queue:
    def __init__(self):
        self.__queue = []
        
    def add(self, item):
        self.__queue.append(item)
        
    def next(self):
        if len(self.__queue) != 0:
            return self.__queue.pop(0)
        else:
            return 0
    
    def is_empty(self):
        return (len(self.__queue) == 0)