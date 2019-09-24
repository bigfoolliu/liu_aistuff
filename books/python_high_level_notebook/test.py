class A(object):
	
	def print(self):
		print("this is method")

	@classmethod
	def method_print(cls):
		print("this is class method")


a = A()
a.print()
a.method_print()
A.print(self)
A.method_print()

