print ("Please input wendu :")
w = int ( input() )

print ('Please input shidu :')
x = int ( input() )

def shidulix (x) :
	if 0 < x <= 25 :
		y = (-1/25) * x + 1
	else :
		y = 0
	return y 

def shiduliz (x) :
	if 15 <= x <= 30 :
		y = (1/15) * x - 1
	elif 30 < x < 45 :
		y = (-1/15) * x + 3
	else :
		y = 0
	return y 

def shidulid (x) :
	if x >= 35 :
		y = (1/25) * x - (7/5)
	else :
		y = 0
	return y 

def wendulid (w) :
	if 0 < w <= 25 :
		y = (-1/25) * w + 1
	else :
		y = 0
	return y

def wenduliz (w) :
	if 0 <= w <= 25 :
		y = (1/25) * w
	elif 25 < w < 50 :
		y = (-1/25) * w + 2 
	else :
		y = 0
	return y

def wendulijg (w) :
	if 25 <= w <= 50 :
		y = (1/25) * w - 1
	elif 50 < w < 75 :
		y = (-1/25) * w + 3 
	else : 
		y = 0
	return y 

def wendulig (w) :
	if 50 <= w <= 75 :
		y = (1/25) * w - 2
	elif 75 < w < 100 :
		y = (-1/25) * w + 4  
	else :
		y = 0
	return y 

d = {'低' : wendulid(w), '中' : wenduliz(w), '较高' : wendulijg(w), '高' : wendulig(w)}
print (d)

c = {'小' : shidulix(x), '中' : shiduliz(x), '大' : shidulid(x)}
print (c)

duan = [min (wendulid(w),shiduliz(x)), min (wenduliz(w),shiduliz(x)), min (wendulijg(w),shiduliz(x)), min (wenduliz(w),shidulid(x))]

zhong = [min (wendulid(w), shidulix(x)), min (wenduliz(w), shidulix(x)), min (wendulig(w),shiduliz(x)), min (wendulig(w), shidulid(x)), min (wendulijg(w),shidulid(x))]

chang = [min (wendulid(w),shidulid(x)), min (wendulijg(w),shidulix(x)), min (wendulig(w),shidulix(x))]

Duan = max (duan)

Zhong = max (zhong)

Chang = max (chang)

u = (Duan * 100 + Zhong * 500 + Chang * 1000)/(Duan + Zhong + Chang)

print ('所需的时间为： ', u) 