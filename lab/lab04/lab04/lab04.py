# Q2
def if_this_not_that(i_list, this):
	"""Define a function which takes a list of integers `i_list` and an integer
	`this`. For each element in `i_list`, print the element if it is larger
	than `this`; otherwise, print the word "that".

	>>> original_list = [1, 2, 3, 4, 5]
	>>> if_this_not_that(original_list, 3)
	that
	that
	that
	4
	5
	"""
	"*** YOUR CODE HERE ***"
	for i in i_list:
		if i<=this:
			print("that") 
		else:
			print(i)	
# Q4
def coords(fn, seq, lower, upper):
	"""
	>>> seq = [-4, -2, 0, 1, 3]
	>>> fn = lambda x: x**2
	>>> coords(fn, seq, 1, 9)
	[[-2, 4], [1, 1], [3, 9]]
	"""
	"*** YOUR CODE HERE ***"
	return [[value, fn(value)] for value in seq if lower<=fn(value)<= upper]

# Q5
def make_city(name, lat, lon):
	"""
	>>> city = make_city('Berkeley', 0, 1)
	>>> get_name(city)
	'Berkeley'
	>>> get_lat(city)
	0
	>>> get_lon(city)
	1
	"""
	return [name, lat, lon]

def get_name(city):
	"""
	>>> city = make_city('Berkeley', 0, 1)
	>>> get_name(city)
	'Berkeley'
	"""
	return city[0]

def get_lat(city):
	"""
	>>> city = make_city('Berkeley', 0, 1)
	>>> get_lat(city)
	0
	"""
	return city[1]

def get_lon(city):
	"""
	>>> city = make_city('Berkeley', 0, 1)
	>>> get_lon(city)
	1
	"""
	return city[2]

from math import sqrt
def distance(city1, city2):
	"""
	>>> city1 = make_city('city1', 0, 1)
	>>> city2 = make_city('city2', 0, 2)
	>>> distance(city1, city2)
	1.0
	>>> city3 = make_city('city3', 6.5, 12)
	>>> city4 = make_city('city4', 2.5, 15)
	>>> distance(city3, city4)
	5.0
	"""
	"*** YOUR CODE HERE ***"
	return sqrt((city1[1]-city2[1])**2 + (city1[2]-city2[2])**2)

# Q6
def closer_city(lat, lon, city1, city2):
	"""
	Returns the name of either city1 or city2, whichever is closest to
	coordinate (lat, lon).

	>>> berkeley = make_city('Berkeley', 37.87, 112.26)
	>>> stanford = make_city('Stanford', 34.05, 118.25)
	>>> closer_city(38.33, 121.44, berkeley, stanford)
	'Stanford'
	>>> bucharest = make_city('Bucharest', 44.43, 26.10)
	>>> vienna = make_city('Vienna', 48.20, 16.37)
	>>> closer_city(41.29, 174.78, bucharest, vienna)
	'Bucharest'
	"""
	"*** YOUR CODE HERE ***"
	temp_city= ("Concrete Jungle", lat, lon)
	distance_city1= distance(temp_city, city1)
	distance_city2= distance(temp_city, city2)

	if distance_city1< distance_city2:
		return get_name(city1)
	return get_name(city2) 

