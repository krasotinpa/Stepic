class ExtendedStack(list):
	def sum(self):
		# операция сложения
		self.append(self.pop()+self.pop())

	def sub(self):
		# операция вычитания
		self.append(self.pop()-self.pop())

	def mul(self):
		# операция умножения
		self.append(self.pop()*self.pop())

	def div(self):
		# операция целочисленного деления
		self.append(self.pop() // self.pop())

a = ExtendedStack([1,2,3,4,5,6])
print(a)
a.sum()
print(a)
a.sub()
print(a)
a.mul()
print(a)
a.div()
print(a)
