class chain_list () :
	def __init__ (self) :
		self.key = []
		self.value = []

	def Insert (self) :
		print("Please input key's location and key :")
		x = int(input())
		self.key.insert(x, str(input()))
		print('Please input the value')
		self.value.insert(x, str(input()))
		# irrelevant codes
		# print(self.key)
		# print(self.value)

	def Delete (self) :
		# z = dict(zip(self.key, self.value))
		# print(z)
		print('Please input what location do you want to delete :')
		y = int(input())
		del(self.key[y-1])
		del(self.value[y-1])
		x = dict(zip(self.key, self.value))
		print(x)

	def Find (self) :
		x = dict(zip(self.value, self.key))
		print('Please input what do you want to find :')
		y = str(input())
		if y in x :
			print('Success!')
			z = x[y]
			print(z)
		else :
			print('Failed')

	def change (self) :
		x = dict(zip(self.key, self.value))
		print(x)

chain = chain_list()

def Tips () :
	print('Please input your choice :')
	print('1.Insert')
	print('2.Find')
	print('3.Delete')

while True :
	Tips()
	x = int(input())

	if x == 1 :
		chain.Insert()
	elif x == 2 :
		chain.Find()
	elif x == 3 :
		chain.Delete()
	else :
		print('Have no this choice')
		break