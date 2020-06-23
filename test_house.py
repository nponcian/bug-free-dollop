class Kitchen(object):
	def __init__(self):
		self.name = 'real'

class Bedroom(object):
	def __init__(self):
		self.name = 'real'

class House(object):
	def __init__(self):
		self.kitchen = Kitchen()
		self.bedroom = Bedroom()

def test_house():
	# TODO test car with dummy kitchen and bedroom
	# assert house.bedroom.name == 'dummy'
	# assert house.kitchen.name == 'dummy'