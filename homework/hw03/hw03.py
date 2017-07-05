HW_SOURCE_FILE = 'hw03.py'

#############
# Questions #
#############

def g(n):
	"""Return the value of G(n), computed recursively.

	>>> g(1)
	1
	>>> g(2)
	2
	>>> g(3)
	3
	>>> g(4) # g(3) + 2*g(2) + 3* g(1)= 3+4+3=10 
	10
	>>> g(5)
	22
	>>> from construct_check import check
	>>> check(HW_SOURCE_FILE, 'g', ['While', 'For'])
	True
	"""
	"*** YOUR CODE HERE ***"

	if n<=3: 
		return n 
	return g(n-1)+ 2*g(n-2) +3* g(n-3)

def g_iter(n):
	"""Return the value of G(n), computed iteratively.

	>>> g_iter(1)
	1
	>>> g_iter(2)
	2
	>>> g_iter(3)
	3
	>>> g_iter(4)
	10
	>>> g_iter(5)
	22
	>>> from construct_check import check
	>>> check(HW_SOURCE_FILE, 'g_iter', ['Recursion'])
	True
	"""
	total=0
	G= [1,2,3]
	for i in range(1, n+1):
		if i>3: 
			G.append(G[i-2] + 2*G[i-3] +3*G[i-4])
	return G[n-1]
def has_seven(k):
	"""Returns True if at least one of the digits of k is a 7, False otherwise.

	>>> has_seven(3)
	False
	>>> has_seven(7)
	True
	>>> has_seven(2734)
	True
	>>> has_seven(2634)
	False
	>>> has_seven(734)
	True
	>>> has_seven(7777)
	True
	"""
	"*** YOUR CODE HERE ***"
	k_string= str(k)
	for i in range(0,len(k_string)):
		if k_string[i]=="7":
			return True 
	return False

def pingpong(n):
	"""Return the nth element of the ping-pong sequence.

	>>> pingpong(7)
	7
	>>> pingpong(8)
	6
	>>> pingpong(15)
	1
	>>> pingpong(21)
	-1
	>>> pingpong(22)
	0
	>>> pingpong(30)
	6
	>>> pingpong(68)
	2
	>>> pingpong(69)
	1
	>>> pingpong(70)
	0
	>>> pingpong(71)
	1
	>>> pingpong(72)
	0
	>>> pingpong(100)
	2
	>>> from construct_check import check
	>>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
	True
	"""
	# i=1 
	# num=1 
	# change_direction=1
	# while i<n :
	# 	#print(num)
	# 	if i%7==0 or has_seven(i): 
	# 		change_direction*=-1 

	# 	num+= change_direction
	# 	i+=1
	# return num


	def helper1(num, change_direction):
		
		if num<=7:
			return num, change_direction
		elif (num-1)%7==0 or has_seven(num-1): 	
			return helper1(num-1, change_direction)[0]+ helper1(num-1, change_direction)[1]*-1, helper1(num-1, change_direction)[1]*-1
		else: 
			return helper1(num-1, change_direction)[0]+ helper1(num-1, change_direction)[1], helper1(num-1, change_direction)[1]
	return helper1(n, 1)[0]


def count_change(amount):
	"""Return the number of ways to make change for amount.

	>>> count_change(7)
	6
	>>> count_change(10)
	14
	>>> count_change(20)
	60
	>>> count_change(100)
	9828
	"""
	"*** YOUR CODE HERE ***"
	coins=0
	for i in range(0, amount):
		if 2**i <=amount:
			coins+=1 
		else:
			break
	#print(coins) 
	if amount<0:
		return 0
	# corresponds to minimum number of coins
	if amount ==0 or amount ==1:
		return 1
	else: 
		with_high_coin= count_change(amount-2 )#amount-2**(coins-1))
		without_high_coin= count_change(amount-coins+1)
	# return without_high_coin + with_high_coin
	return with_high_coin +without_high_coin

def print_move(origin, destination):
	"""Print instructions to move a disk."""
	print("Move the top disk from rod", origin, "to rod", destination)

def move_stack(n, start, end):
	"""Print the moves required to move n disks on the start pole to the end
	pole without violating the rules of Towers of Hanoi.

	n -- number of disks
	start -- a pole position, either 1, 2, or 3
	end -- a pole position, either 1, 2, or 3

	There are exactly three poles, and start and end must be different. Assume
	that the start pole has at least n disks of increasing size, and the end
	pole is either empty or has a top disk larger than the top n start disks.

	>>> move_stack(1, 1, 3)
	Move the top disk from rod 1 to rod 3
	>>> move_stack(2, 1, 3)
	Move the top disk from rod 1 to rod 2
	Move the top disk from rod 1 to rod 3
	Move the top disk from rod 2 to rod 3
	>>> move_stack(3, 1, 3)
	Move the top disk from rod 1 to rod 3
	Move the top disk from rod 1 to rod 2
	Move the top disk from rod 3 to rod 2
	Move the top disk from rod 1 to rod 3
	Move the top disk from rod 2 to rod 1
	Move the top disk from rod 2 to rod 3
	Move the top disk from rod 1 to rod 3
	"""
	assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
	"*** YOUR CODE HERE ***"
	if n==1 : 
		print_move(start, end)	
	else:
		middle_peg= 6-start-end
		move_stack(n-1, start,middle_peg) 	
		move_stack(1,start, end)
		move_stack(n-1, middle_peg, end)

	#

def flatten(lst):
	"""Returns a flattened version of lst.

	>>> flatten([1, 2, 3])     # normal list
	[1, 2, 3]
	>>> x = [1, [2, 3], 4]      # deep list
	>>> flatten(x)
	[1, 2, 3, 4]
	>>> x = [[1, [1, 1]], 1, [1, 1]] # deep list
	>>> flatten(x)
	[1, 1, 1, 1, 1, 1]
	"""
	"*** YOUR CODE HERE ***"
	flat_list=[]
	if type(lst[0])!=list: 
		flat_list= [lst[0]]+ flat_list
	else:
		flat_list= int(lst[0][0])
		#	return int(lst[0])		 


def merge(lst1, lst2):
	"""Merges two sorted lists.

	>>> merge([1, 3, 5], [2, 4, 6])
	[1, 2, 3, 4, 5, 6]
	>>> merge([], [2, 4, 6])
	[2, 4, 6]
	>>> merge([1, 2, 3], [])
	[1, 2, 3]
	>>> merge([5, 7], [2, 4, 6])
	[2, 4, 5, 6, 7]
	"""
	"*** YOUR CODE HERE ***"
	#combine_list= lst1 +lst2 
	#def sorted(lst1,lst2):
	sorted_list=[]
	if lst1!= [] and lst2 !=[]:
		if lst1[0]>lst2[0]:
			lst1[0],lst2[0]= lst2[0],lst1[0]
		return sorted_list + [lst1[0]]+ merge(lst1[1:],lst2)
	return lst1 + lst2
def mergesort(seq):
	"""Mergesort algorithm.

	>>> mergesort([4, 2, 5, 2, 1])
	[1, 2, 2, 4, 5]
	>>> mergesort([])     # sorting an empty list
	[]
	>>> mergesort([1])   # sorting a one-element list
	[1]
	"""
	"*** YOUR CODE HERE ***"
