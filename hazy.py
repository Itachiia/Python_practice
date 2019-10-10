class Function () :
	def __init__ (self) :
		self.humidty = 0
		self.temperature = 0
		self.temperature_degree = []
		self.humidty_degree = []
		self.min_time_short = []
		self.min_time_middle = []
		self.min_time_long = []
		self.max_time_short = []
		self.max_time_middle = []
		self.max_time_long = []
		self.result = []

	def run (self) :
		for i in range(5) :
			self.humidty = int(input())
			self.temperature = int(input())
			self.humidty_degree.append(self.humidtysmall())
			self.humidty_degree.append(self.humidtymiddle())
			self.humidty_degree.append(self.humidtyhigh())
			self.temperature_degree.append(self.temperaturelow())
			self.temperature_degree.append(self.temperaturemiddle())
			self.temperature_degree.append(self.temperature_high())
			self.temperature_degree.append(self.temperaturehigh())
			self.min_time_short.append(self.min_short())
			self.min_time_middle.append(self.min_middle())
			self.min_time_long.append(self.min_long())
			self.max_time_short.append(self.max_min_short())
			self.max_time_middle.append(self.max_min_middle())
			self.max_time_long.append(self.max_min_long())
			self.humidty_degree.clear()
			self.temperature_degree.clear()
			self.min_time_short.clear()
			self.min_time_middle.clear()
			self.min_time_long.clear()
			self.max_time_short.clear()
			self.max_time_middle.clear()
			self.max_time_long.clear()

			self.result.append(self.result_())

			print(self.result)

	def humidtysmall (self) :
		if 0 < self.humidty <= 25 :
			degree = (-1/25) * self.humidty + 1
		else :
			degree = 0
		return degree

	def humidtymiddle (self) :
		if 15 <= self.humidty <= 30:
			degree = (1/15) * self.humidty - 1
		elif 30 < self.humidty < 45 :
			degree = (-1/15) * self.humidty + 3
		else :
			degree = 0
		return degree

	def humidtyhigh (self) :
		if self.humidty >= 35 :
			degree = (1/25) * self.humidty - (7/5)
		else :
			degree = 0
		return degree

	def temperaturelow (self):
		if 0 <= self.temperature <= 25 :
			degree = (-1/25) * self.temperature + 1
		else :
			degree = 0
		return degree

	def temperaturemiddle (self) :
		if 0 <= self.temperature <= 25 :
			degree = (1/25) * self.temperature
		elif 25 < self.temperature < 50 :
			degree = (-1/25) * self.temperature + 2
		else :
			degree = 0
		return degree

	def temperature_high (self) :
		if 25 <= self.temperature <= 50 :
			degree = (1/25) * self.temperature - 1
		elif 50 < self.temperature < 75 :
			degree = (-1/25) * self.temperature + 3
		else :
			degree = 0
		return degree

	def temperaturehigh (self) :
		if 50 <= self.temperature <= 75 :
			degree = (1/25) * self.temperature - 2
		elif 75 < self.temperature < 100 :
			degree = (-1/25) * self.temperature + 4
		else :
			degree = 0
		return degree

	# Degree = [humidtysmall(self.humidty), humidtymiddle(self.humidty, humidtybig(self.humidty))]

	# print (Degree)

	# x = [humidtysmall(humidty)]
	# print (x)

	# def min_humidty (self, humidtysmall(self.humidty), humidtymiddle(self.humidty), humidtybig(self.humidty)) :
		# self.minimum = min (humidtysmall(self.humidty), humidtymiddle(self.humidty), humidtybig(self.humidty))
		# return self.minimum

	# def min_temperature (self, temperaturelow(self.temperature), temperaturemiddle(self.temperature), temperature_high(self.temperature), temperaturehigh(self.temperature)) :
		# self.minimum = min (temperaturelow(self.temperature), temperaturemiddle(self.temperature), temperature_high(self.temperature), temperaturehigh(self.temperature))
		# return self.minimum

	def min_short (self) :
		mi = [min(self.temperaturelow(), self.humidtymiddle()), min(self.temperaturemiddle(), self.humidtymiddle()),
		 min(self.temperature_high(),self.humidtymiddle()), min(self.temperaturemiddle(),self.humidtyhigh())]
		return mi

	def min_middle (self) :
		mi = [min(self.temperaturelow(),self.humidtysmall()), min(self.temperaturemiddle(),self.humidtysmall()), min(self.temperaturehigh(),self.humidtymiddle()), min(self.temperaturehigh(),self.humidtyhigh()), min(self.temperature_high(),self.humidtyhigh())]
		return mi

	def min_long (self) :
		mi = [min(self.temperaturelow(),self.humidtyhigh()), min(self.temperature_high(),self.humidtysmall()), min(self.temperaturehigh(),self.humidtysmall())]
		return mi

	def max_min_short (self) :
		ma = max(self.min_short())
		return ma

	def max_min_middle (self) :
		ma = max(self.min_middle())
		return ma

	def max_min_long (self) :
		ma = max(self.min_long())
		return ma

	def result_ (self) :
		re = (self.max_min_short() * 100 + self.max_min_middle() * 500 + self.max_min_long() * 1000)/(self.max_min_short() + self.max_min_middle() + self.max_min_long())
		return re

fuzzy = Function()
fuzzy.run()