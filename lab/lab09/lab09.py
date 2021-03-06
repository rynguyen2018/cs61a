# Q1
class ScaleIterator:
    """An iterator the scales elements of the iterable s by a number k.

    >>> s = ScaleIterator([1, 5, 2], 5)
    >>> for elem in s:
    ...     print(elem)
    5
    25
    10
    >>> m = ScaleIterator([1, 2, 3, 4, 5, 6], 2)
    >>> [next(m) for _ in range(5)]
    [2, 4, 6, 8, 10]
    """
    def __init__(self, s, k):
        "*** YOUR CODE HERE ***"
        self.lst= iter(s)
        self.scale= k 

    def __iter__(self):
        return self

    def __next__(self):
        "*** YOUR CODE HERE ***"
        elem= next(self.lst) 
        if elem: 
            return elem*self.scale
        else:
            raise StopIteration