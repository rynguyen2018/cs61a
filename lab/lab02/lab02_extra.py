"""Optional program for lab02 """

from lab02 import *

# Higher Order Functions

def count_cond(condition):
    """Returns a function with one parameter N that counts all the numbers from
    1 to N that satisfy the two-argument predicate function CONDITION.

    >>> count_factors = count_cond(lambda n, i: n % i == 0)
    >>> count_factors(2)   # 1, 2
    2
    >>> count_factors(4)   # 1, 2, 4
    3
    >>> count_factors(12)  # 1, 2, 3, 4, 6, 12
    6

    >>> is_prime = lambda n, i: count_factors(i) == 2
    >>> count_primes = count_cond(is_prime)
    >>> count_primes(2)    # 2
    1
    >>> count_primes(3)    # 2, 3
    2
    >>> count_primes(4)    # 2, 3
    2
    >>> count_primes(5)    # 2, 3, 5
    3
    >>> count_primes(20)   # 2, 3, 5, 7, 11, 13, 17, 19
    8
    """
    "*** YOUR CODE HERE ***"
    def counter(x):
        count =0 
        for i in range(1,x+1):
            if condition(x,i):
                count+=1
        return count 
    return counter

def cycle(f1, f2, f3):
    """Returns a function that is itself a higher-order function.

    >>> def add1(x):
    ...     return x + 1
    >>> def times2(x):
    ...     return x * 2
    >>> def add3(x):
    ...     return x + 3
    >>> my_cycle = cycle(add1, times2, add3)
    >>> identity = my_cycle(0)
    >>> identity(5)
    5
    >>> add_one_then_double = my_cycle(2)
    >>> add_one_then_double(1)
    4
    >>> do_all_functions = my_cycle(3)
    >>> do_all_functions(2)
    9
    >>> do_more_than_a_cycle = my_cycle(4)
    >>> do_more_than_a_cycle(2)
    10
    >>> do_two_cycles = my_cycle(6)
    >>> do_two_cycles(1)
    19
    """
    function_list= [f1,f2,f3]
    
    def call_function(num_calls): 
        def do_function(y):
            total =y 
            if num_calls==0: 
                return total
            for x in range(0,num_calls):
                if x< 3:
                    total=function_list[x](total)
                else:
                    total= function_list[x%3](total)
                #print(total)
                #print(total) 
            return total 
        return do_function
    return call_function    

def add1(x):
    #print("adding 1")
    return x + 1
def times2(x):
    #print("mult 2")
    return x * 2
def add3(x):
    #print("add3")
    return x + 3