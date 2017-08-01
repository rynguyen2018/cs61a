from stream import *

def countdown(n):
    """
    A generator that counts down from N to 0.
    >>> for number in countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    >>> for number in countdown(2):
    ...     print(number)
    ...
    2
    1
    0
    """
    "*** YOUR CODE HERE ***"
    while n>=0 :
        yield n
        n=n-1

def trap(s, k):
    """Return a generator that yields the first K values in iterable S,
    but raises a ValueError exception if any more values are requested.

    >>> t = trap([3, 2, 1], 2)
    >>> next(t)
    3
    >>> next(t)
    2
    >>> next(t)
    ValueError
    >>> list(trap(range(5), 5))
    ValueError
    """
    assert len(s) >= k
    "*** YOUR CODE HERE ***"
    i=0 
    while i < k: 
        yield s[i]
        i+=1 
    raise ValueError

def repeated(t, k):
    """Return the first value in iterable T that appears K times in a row.

    >>> s = [3, 2, 1, 2, 1, 4, 4, 5, 5, 5]
    >>> repeated(trap(s, 7), 2)
    4
    >>> repeated(trap(s, 10), 3)
    5
    >>> print(repeated([4, None, None, None], 3))
    None
    """
    assert k > 1
    "*** YOUR CODE HERE ***"
    if isinstance(t, list):
        t= trap(t, len(t))
    num_appearances= 1
    try: 
        elem1= next(t)
        while True: 
            elem2= next(t)
            if elem1== elem2: 
                num_appearances+=1  
                if num_appearances ==k :
                    return elem1
            elem1= elem2
    except StopIteration: 
       pass

ones = None

def ones_test():
    """
    >>> ones.first, ones.rest.first, ones.rest.rest.first, ones.rest.rest.rest.first
    (1, 1, 1, 1)
    """
    #ones=1
    def compute_rest():
        return ones_test()
    return Stream(1, compute_rest)
ones= ones_test()
def scan(f, initial_value, stream):
    """
    >>> ones = Stream(1, lambda: ones)
    >>> naturals = scan(lambda x, y: x + y, 1, ones)
    >>> _ = naturals.rest.rest.rest
    >>> naturals
    Stream(1, Stream(2, Stream(3, Stream(4, <...>))))
    >>> factorials = scan(lambda x, y: x * y, 1, naturals)
    >>> _ = factorials.rest.rest.rest.rest
    >>> factorials
    Stream(1, Stream(1, Stream(2, Stream(6, Stream(24, <...>)))))
    """
    "*** YOUR CODE HERE ***"
    def compute_rest(): 
        value= f(initial_value, stream.first)
        return scan(f, value, stream.rest)
    return Stream(initial_value, compute_rest) 

