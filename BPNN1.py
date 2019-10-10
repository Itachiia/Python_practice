# 三层神经网络；3 2 1
# 期望值 ： 2
# 激活函数 ： Sigmoid

import math

from random import uniform as u #调用random函数生成随机数
"""
T_T = 1

L = 1/12

W = [uni(0,10),uni(0,10),uni(0,10),uni(0,10),uni(0,10),uni(0,10),uni(0,10),uni(0,10)] 	#随机生成权重值
Theta = [uni(0,10),uni(0,10),uni(0,10)] 	#随机生成神经元偏置
X = [uni(0,10),uni(0,10),uni(0,10)]		#随机生成输入样本

def Net (W, Theta, X) :		#定义net
	N = W *X +Theta
	return N 

def Sig (N) :		#定义激活函数
	O = 1.0 / (1 + math.exp(-N))
	return O

def Sig_derivative () :		#定义激活函数的导数
	O_O = t * (1-t)
	return O_O

def Error_1 (O_O) :		#计算输出层误差
	E_1 = O_O * (T_T - O)
	return E_1

def Error_2 (O_O, E, W) :		#计算隐含层误差
	E_2 = O_O * E_1 * W
	return E_2

def Update (W, L, Theta) :		#计算更新后的权重
	W = W + L * E_2 * X
	return W
	"""

class BPNN () :
	def __init__ (self) :
		self.input = [u(0,10),u(0,10),u(0,10)]
		self.weight = [u(0,10),u(0,10),u(0,10),u(0,10),u(0,10),u(0,10),u(0,10),u(0,10)]
		self.theta = [u(0,10),u(0,10),u(0,10)]

	def Net (self, )

