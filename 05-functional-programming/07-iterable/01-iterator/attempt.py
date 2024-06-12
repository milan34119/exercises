# Here, `range(10)` creates a `range`-object.
# This object is _iterable_, but not an _iterator_.
# The `for`-loop needs an _iterator_`, so it uses `iter` to have the iterable create an iterator.
# Calling `next` on this iterator produces all the elements of the range.

# Create your own `InclusiveRange` (= iterable) and accompanying `InclusiveRangeIterator` (=iterator) class.
# It should be usable as follows:

# ```python
# >>> for i in InclusiveRange(1, 5)
# ...     print(i)
# 1
# 2
# 3
# 4
# 5
# ```

# For this to work, `InclusiveRange` needs an `__iter__` method that returns a `InclusiveRangeIterator` object.
# `InclusiveRangeIterator` should implement `__iter__` (just have it return `self`) and `__next__`.

# Note that `InclusiveRange` should be reusable, but `InclusiveRangeIterator` should be single use:
class InclusiveRange:
    def __init__(self, start, end):
        self.__start = start
        self.__end = end

    def __iter__(self):
        return InclusiveRangeIterator(self.__start, self.__end)
    
class InclusiveRangeIterator:
    def __init__(self, start, end):
        self.__current = start
        self.__end = end
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.__current <= self.__end:
            result = self.__current
            self.__current += 1
            return result
        else:
            raise StopIteration
    