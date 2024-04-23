# Private methods are accessible outside their class, just not easily accessible. Nothing in Python is truly private; internally, the names of private methods and attributes are mangled and unmangled on the fly to make them seem inaccessible by their given names
# A Python program to demonstrate that hidden 
# members can be accessed outside a class 
# class MyClass: 
# 	# private member of MyClass 
# 	__hiddenVariable = 10
# myObject = MyClass()	 
# print(myObject._MyClass__hiddenVariable) 

class Test: 
	def __init__(self, a, b): 
		self.a = a 
		self.b = b 

	def __repr__(self): 
		return "Test a:%s b:%s" % (self.a, self.b) 

	# def __str__(self): 
	# 	return "From str method of Test: a is %s," \
	# 	"b is %s" % (self.a, self.b) 

# Driver Code		 
t = Test(1234, 5678) 
print(t) # This calls __str__() 
# print([t]) # This calls __repr__() 
