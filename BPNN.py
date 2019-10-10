# 引用数学算法库
import math

# 3层神经网络
#定义权重
print("请输入网络连接权重w：")
w14 = float (input("w14 = "))
w15 = float (input("w15 = "))
w24 = float (input("w24 = "))
w25 = float (input("w25 = "))
w34 = float (input("w34 = "))
w35 = float (input("w35 = "))
w46 = float (input("w46 = "))
w56 = float (input("w56 = "))

# 定义神经元偏置
print("请输入神经元偏置theta：")
theta4 = float (input("theta4 = "))
theta5 = float (input("theta5 = "))
theta6 = float (input("theta6 = "))

# 定义学习率
print("请输入学习率l：")
l = float (input("l = "))

# 输入
print("请输入训练样本:")
O1 = int (input("O1 = "))
O2 = int (input("O2 = "))
O3 = int (input("O3 = "))

net4 = w14*O1 + w24*O2 + w34*O3 + theta4
net5 = w15*O1 + w25*O2 + w35*O3 + theta5

# 计算4节点输出
O4 = 1/(1 + math.e**-net4)

# 计算5节点的输出
O5 = 1/(1 + math.e**-net5)

net6 = w46*O4+w56*O5+theta6

# 计算节点6的输出
O6 = 1/(1 + math.e**-net6)

# 计算误差
E6 = O6 * (1-O6) * (1-O6) 
E5 = O5 * (1-O5) * E6 * w56
E4 = O4 * (1-O4) * E6 * w46

# 更新后的权重
print("w46 = ", w46 + l * E6 * O4)
print("w56 = ", w56 + l * E6 * O5)
print("w14 = ", w14 + l * E4 * O1)
print("w24 = ", w24 + l * E4 * O2)
print("w34 = ", w34 + l * E4 * O3)
print("w15 = ", w15 + l * E5 * O1)
print("w25 = ", w25 + l * E5 * O2)
print("w35 = ", w35 + l * E5 * O3)

# 更新后的神经元偏置
print("theta4 = ", theta4 + l * E4)
print("theta5 = ", theta5 + l * E5)
print("theta6 = ", theta6 + l * E6)