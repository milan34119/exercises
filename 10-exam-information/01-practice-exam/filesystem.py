# Enter your code here:
class StorageDevice:
    def __init__(self, block_count, block_size):
        self.__available_blocks = set(range(0, block_count))
        self.__used_blocks = set()
        self.__block_size = block_size
        
    @property
    def available_block_count(self):
        return self.__available_blocks
    
    @property
    def used_block_count(self):
        return self.__used_blocks
    
    @property
    def total_block_count(self):
        return (self.__available_blocks + self.__used_blocks)
    
    @property
    def block_size(self):
        return self.__block_size
    
    