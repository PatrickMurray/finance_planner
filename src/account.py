class Account:
	def __init__(self):
		self.balance = 0

		return


	def deposit(self, amount: int):
		self.balance += amount

		return


	def withdraw(self, amount: int):
		self.balance -= amount

		return
