class computer:

	def __init__(self, cpu, ram):
		self.cpu = cpu
		self.ram = ram

	def config(self):
		print("config is", self.cpu, self.ram)



com1 = computer("i5", 16)
com2 = computer("ryzen 5", 32)

print(com1.config())

computer.config(com1)
computer.config(com2)

print(com1.cpu)