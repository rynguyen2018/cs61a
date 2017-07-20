## List Mutation ##
def map(fn, lst):
    """Maps fn onto lst using mutation.
    >>> original_list = [5, -1, 2, 0]
    >>> map(lambda x: x * x, original_list)
    >>> original_list
    [25, 1, 4, 0]
    """
    "*** YOUR CODE HERE ***"
    for x in range(0,len(lst)): 
        lst[x]= fn(lst[x])
    #lst=[fn(element) for element in lst]
def filter(pred, lst):
    """Filters lst with pred using mutation.
    >>> original_list = [5, -1, 2, 0]
    >>> filter(lambda x: x % 2 == 0, original_list)
    >>> original_list
    [2, 0]

    """
    lst2= lst[:]
    "*** YOUR CODE HERE ***"
    for x in range(0,len(lst)): 
        lst.pop()
        #if pred(lst[x])==True:
    
    for y in range(0, len(lst2)):
        if pred(y)==True:
            lst.insert(0, y)


## Dictionaries ##

def replace_all(d, x, y):
    """Replace all occurrences of x as a value (not a key) in d with y.
    >>> d = {3: '3', 'foo': 2, 'bar': 3, 'garply': 3, 'xyzzy': 99}
    >>> replace_all(d, 3, 'poof')
    >>> d == {3: '3', 'foo': 2, 'bar': 'poof', 'garply': 'poof', 'xyzzy': 99}
    True
    """
    "*** YOUR CODE HERE ***"
    for key in d: 
        if d[key]==x:
            d[key]=y


