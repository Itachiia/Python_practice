# 真实世界中很少会要求精确到普通浮点数能提供的17位精度，执行大量运算的时候速度很重要。所以使用不要随便用decimal.
from decimal import Decimal
a = 1.1
b = 2.7
print('a + b = ',a + b)