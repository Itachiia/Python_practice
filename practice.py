from random import uniform
from random import randrange

class function () :
	def __init__ (self) :
		self.user = []
		self.music = []

	def run_user (self) :
		for i in range (5) :
			self.user.append(self.User())

	def run_music (self) :
		for i in range (10) :
			self.music.append(self.Music())

	def User (self) :
		for i in range(5) :
			self.user.append(i)
		return self.user

	def Music (self) :
		for i in range(10) :
			self.music.append(i)
		return self.music

U = function()
U.run_user()
U.run_music()

# 1.用什么样的数据类型来表示数据量？ （字典、集合、列表？）
# 2.求相似 取交集
# b = 6 if 5 > 12 else 9
# while 一般用于循环次数不确定的情况，而for一般用于循环次数确定的情况
# swicth.default c language
