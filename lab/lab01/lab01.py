"""Lab 1: Expressions and Control Structures"""

# Coding Practice

def repeated(f, n, x):
    """Returns the result of composing f n times on x.

    >>> def square(x):
    ...     return x * x
    ...
    >>> repeated(square, 2, 3)  # square(square(3)), or 3 ** 4
    81
    >>> repeated(square, 1, 4)  # square(4)
    16
    >>> repeated(square, 6, 2)  # big number
    18446744073709551616
    >>> def opposite(b):
    ...     return not b
    ...
    >>> repeated(opposite, 4, True)
    True
    >>> repeated(opposite, 5, True)
    False
    >>> repeated(opposite, 631, 1)
    False
    >>> repeated(opposite, 3, 0)
    True
    """
    "*** YOUR CODE HERE ***"
    num_iter=n 
    current_iter=0
    current_answer= x 
    new_answer=0

    while (current_iter < num_iter):
        new_answer= f(current_answer)
        current_answer= new_answer
        current_iter+=1
    return new_answer

def sum_digits(n):
    """Sum all the digits of n.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    """

    number_list= list(str(n))
    summ=0
    for num in number_list: 
        summ += int(num)
    #print(summ)
    return summ

def double_eights(n):
	isDouble= False 
	last_num=0
	penult_num=0
	while n: 
		last_num= n%10
		penult_num= (n//10)%10 
		
		if last_num== penult_num and last_num==8: 
			isDouble=True
			break 
		else: 
			 n//=10
	return isDouble

