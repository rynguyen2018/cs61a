############
# Mutation #
############

def make_withdraw(balance, password):
	"""Return a password-protected withdraw function.

	>>> w = make_withdraw(100, 'hax0r')
	>>> w(25, 'hax0r')
	75
	>>> w(90, 'hax0r')
	'Insufficient funds'
	>>> w(25, 'hwat')
	'Incorrect password'
	>>> w(25, 'hax0r')
	50
	>>> w(75, 'a')
	'Incorrect password'
	>>> w(10, 'hax0r')
	40
	>>> w(20, 'n00b')
	'Incorrect password'
	>>> w(10, 'hax0r')
	"Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
	>>> w(10, 'l33t')
	"Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
	"""
	"*** YOUR CODE HERE ***"
	incorrect=0
	wrong_list=[]
	def withdraw(amount, attempt):
		if attempt != password and len(wrong_list)<3: 
			wrong_list.append(attempt) 
			return "Incorrect password"
		elif len(wrong_list)>=3:
			return "Your account is locked. Attempts: " +  str(wrong_list)
		else: 
			nonlocal balance
			if amount > balance:
				return 'Insufficient funds'
			balance = balance - amount
			return balance
	return withdraw
	

def make_joint(withdraw, old_password, new_password):
	"""Return a password-protected withdraw function that has joint access to
	the balance of withdraw.

	>>> w = make_withdraw(100, 'hax0r')
	>>> w(25, 'hax0r')
	75
	>>> make_joint(w, 'my', 'secret')
	'Incorrect password'
	>>> j = make_joint(w, 'hax0r', 'secret')
	>>> w(25, 'secret')
	'Incorrect password'
	>>> j(25, 'secret')
	50
	>>> j(25, 'hax0r')
	25
	>>> j(100, 'secret')
	'Insufficient funds'

	>>> j2 = make_joint(j, 'secret', 'code')
	>>> j2(5, 'code')
	20
	>>> j2(5, 'secret')
	15
	>>> j2(5, 'hax0r')
	10

	>>> j2(25, 'password')
	'Incorrect password'
	>>> j2(5, 'secret')
	"Your account is locked. Attempts: ['my', 'secret', 'password']"
	>>> j(5, 'secret')
	"Your account is locked. Attempts: ['my', 'secret', 'password']"
	>>> w(5, 'hax0r')
	"Your account is locked. Attempts: ['my', 'secret', 'password']"
	>>> make_joint(w, 'hax0r', 'hello')
	"Your account is locked. Attempts: ['my', 'secret', 'password']"
	"""
	"*** YOUR CODE HERE ***"

	def joint_withdraw(amount, attempt): 
		if attempt== new_password or attempt== old_password: 
			return withdraw(amount, old_password)
		else: 
			return withdraw(amount, attempt)
	x= withdraw(0, old_password)
	if type(x)!=str:
		return joint_withdraw
	return x

###########
# Objects #
###########

class VendingMachine:
	"""A vending machine that vends some product for some price.

	>>> v = VendingMachine('candy', 10)
	>>> v.vend()
	'Machine is out of stock.'
	>>> v.restock(2)
	'Current candy stock: 2'
	>>> v.vend()
	'You must deposit $10 more.'
	>>> v.deposit(7)
	'Current balance: $7'
	>>> v.vend()
	'You must deposit $3 more.'
	>>> v.deposit(5)
	'Current balance: $12'
	>>> v.vend()
	'Here is your candy and $2 change.'
	>>> v.deposit(10)
	'Current balance: $10'
	>>> v.vend()
	'Here is your candy.'
	>>> v.deposit(15)
	'Machine is out of stock. Here is your $15.'

	>>> w = VendingMachine('soda', 2)
	>>> w.restock(3)
	'Current soda stock: 3'
	>>> w.deposit(2)
	'Current balance: $2'
	>>> w.vend()
	'Here is your soda.'
	"""
	"*** YOUR CODE HERE ***"
	def __init__(self, product, price):
		self.product=product 
		self.price=price 
		self.quantity= 0
		self.current_balance=0

	def restock(self, num):
		self.quantity+= num 
		return 'Current '+ self.product + ' stock: ' + str(self.quantity)

	def vend(self):
		if self.quantity==0: 
			return "Machine is out of stock."
		elif self.current_balance< self.price: 
			return 'You must deposit $'+ str(self.price- self.current_balance) + ' more.'
		elif self.quantity==1 or self.price==self.current_balance:
			self.current_balance=0
			self.quantity-=1
			return 'Here is your '+ self.product +'.'
		else: 
			change= self.current_balance-self.price 
			self.current_balance=0
			self.quantity-=1
			return 'Here is your '+ self.product+ ' and $' + str(change) + ' change.' 

	def deposit(self, amount):
		if self.quantity==0: 
			return 'Machine is out of stock. Here is your $' + str(amount) + '.'
		else:
			self.current_balance+= amount 		
			return 'Current balance: $' + str(self.current_balance)

class MissManners:
	"""A container class that only forward messages that say please.

	>>> v = VendingMachine('teaspoon', 10)
	>>> v.restock(2)
	'Current teaspoon stock: 2'

	>>> m = MissManners(v)
	>>> m.ask('vend')
	'You must learn to say please first.'
	>>> m.ask('please vend')
	'You must deposit $10 more.'
	>>> m.ask('please deposit', 20)
	'Current balance: $20'
	>>> m.ask('now will you vend?')
	'You must learn to say please first.'
	>>> m.ask('please hand over a teaspoon')
	'Thanks for asking, but I know not how to hand over a teaspoon.'
	>>> m.ask('please vend')
	'Here is your teaspoon and $10 change.'

	>>> double_fussy = MissManners(m) # Composed MissManners objects
	>>> double_fussy.ask('deposit', 10)
	'You must learn to say please first.'
	>>> double_fussy.ask('please deposit', 10)
	'Thanks for asking, but I know not how to deposit.'
	>>> double_fussy.ask('please please deposit', 10)
	'Thanks for asking, but I know not how to please deposit.'
	>>> double_fussy.ask('please ask', 'please deposit', 10)
	'Current balance: $10'
	"""
	def __init__(self, obj):
		self.obj = obj

	def ask(self, message, *args):
		magic_word = 'please '
		if not message.startswith(magic_word):
			return 'You must learn to say please first.'
		"*** YOUR CODE HERE ***"
		command= message.split()[1]
		if hasattr(self.obj, command):
			function= getattr(self.obj, command)
			if len(args)==1: 
				return function(args[0])
			elif len(args)>1:
				arg1, arg2= args
				return function(arg1,arg2)
			return function()
		else: 
			return 'Thanks for asking, but I know not how to ' + message.split("please ", 1)[1] + '.'