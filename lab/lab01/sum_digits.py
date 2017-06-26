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

#sum_digits(10)
