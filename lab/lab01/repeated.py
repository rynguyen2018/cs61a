def square(x):
	return x * x
def opposite(b):
	return not b	
def repeated(f, n, x):
	num_iter=n 
	current_iter=0
	current_answer= x 
	new_answer=0

	while (current_iter < num_iter):
		new_answer= f(current_answer)
		current_answer= new_answer
		current_iter+=1
	return new_answer
