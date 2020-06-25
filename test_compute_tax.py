class SalesTaxCalculator(object):
	def computeTax(self, user, invoice):
		address = user.address
		amount = invoice.subTotal
		return amount * self.getTaxRate(address)

	def computeTaxUpdated(self, address, amount):
		return amount * self.getTaxRate(address)

	def getTaxRate(self, address):
		if address == 'makati':
			return 0.3

		if address == 'quezon':
			return 0.1

class Invoice(object):
	def __init__(self):
		self.subTotal = 100

class User(object):
	def __init__(self, name, address):
		self.name = name
		self.address = address

def test_compute_tax():
	# TODO test computed tax for makati

	user = User('Batman', 'makati')
	invoice = Invoice()
	calculator = SalesTaxCalculator()

	tax = calculator.computeTax(user, invoice)
	assert tax == 30.0

	tax = calculator.computeTaxUpdated(user.address, invoice.subTotal)
	assert tax == 30.0
