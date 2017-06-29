"""Lab 3: Recursion and Tree Recursion"""

# Q1


def ab_plus_c(a, b, c):
    """Computes a * b + c.

    >>> ab_plus_c(2, 4, 3)  # 2 * 4 + 3
    11
    >>> ab_plus_c(0, 3, 2)  # 0 * 3 + 2
    2
    >>> ab_plus_c(3, 0, 2)  # 3 * 0 + 2
    2
    """
    "*** YOUR CODE HERE ***"
    def ab(a,b): 
        if b==1 or a==0: 
            return a
        elif b==0: 
            return 0
        else: 
            return a+ab(a,b-1)
    return ab(a,b) + c

# Q2
def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    "*** YOUR CODE HERE ***"
    if max(a,b)%min(a,b)==0: 
        return min(a,b)
    else: 
        return gcd(max(a,b)%min(a,b), min(a,b))

# Q3
def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"
    print(n)
    if n==1:
        return 1  

    if n%2==0:
        return hailstone(int(n/2)) +1
    return hailstone(int(3*n+1)) +1



