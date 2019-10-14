class Student() :
	def __init__ (self) :
		self.sid = []
		self.name = []
		self.telephone = []
	#Add student's identification
	def Add_sid (self) :
		print(' Please input your sid :')
		self.sid.append(str(input()))

	# Add student's name
	def Add_name (self) :
		print('Please input your name :')
		self.name.append(str(input()))

	# Add student's telephone number
	def Add_telephone (self) :
		print('Please input your telephone :')
		self.telephone.append(str(input()))

	# Find function
	def Find (self) :
		print('Please input your find number :')
		a = int(input())
		print(self.sid[a-1], self.name[a-1], self.telephone[a-1])

	# Delete function
	def Delete (self) :
		print('Please input your delete number :')
		b = int(input())
		# print(self.sid.pop(b-1), self.name.pop(b-1), self.telephone.pop(b-1)) Output the deleted student's information
		print(self.sid, self.name, self.telephone)

	# Display function
	def Display (self) :
		print('Please input your number :')
		print(self.sid, self.name, self.telephone)

# Invoke class 'Student'
student = Student()

# Tip function
def Tips () :
	print('Please input your choice :')
	print('0.结束')
	print('1.Add')
	print('2.Find')
	print('3.Delete')
	print('4.Display')

while True:
	Tips()
	x = int(input())

	if x == 1:
		student.Add_sid()
		student.Add_name()
		student.Add_telephone()
		# print(student.Add_sid(), student.Add_name(), student.Add_telephone())
	elif x == 2 :
		student.Find()
	elif x == 3 :
		student.Delete()
	elif x == 4 :
		student.Display()
	else :
		break