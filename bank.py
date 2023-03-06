# Class to do...
class Bank_Account:
	def _int_(self, account_number, balance, date_of_opening, customer_name):
		self.account_number = account_number
		self.balance = balance
		self.date_of_opening = date_of_opening
		self.customer_name = customer_name

	def deposit(self, amount):
		self.balance += amount
		return self.balance

	def withdraw(self, amount):
		if self.balance >= amount:
			self.balance -= amount
			return amount
		else:
			return 'Insufficient balance'

	def check_balance(self):
		print(self.balance)

	def customer_details(self):
		print("Name:", self.customer_name)
		print("Account Number:", self.account_number)
		print("Date of Opening:", self.date_of_opening)
		print("Balance:",self.balance)