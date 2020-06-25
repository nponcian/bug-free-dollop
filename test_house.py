class Kitchen(object):
	def __init__(self, name='real'):
		self.name = name

class Bedroom(object):
	def __init__(self, name='real'):
		self.name = name

class House(object):
	def __init__(self, housePartsFactory):
		self.housePartsFactory = housePartsFactory

	def buildKitchen(self, kitchenName):
		self.kitchen = self.housePartsFactory.createKitchen(kitchenName)

	def buildBedroom(self, bedroomName):
		self.bedroom = self.housePartsFactory.createBedroom(bedroomName)

class HousePartsFactory:
	pass

class OrdinaryHousePartsFactory(HousePartsFactory):
	def createKitchen(self, name):
		return Kitchen(name)

	def createBedroom(self, name):
		return Bedroom(name)

def test_house():
	# TODO test car with dummy kitchen and bedroom
	housePartsFactory = OrdinaryHousePartsFactory()
	house = House(housePartsFactory)

	house.buildKitchen('let us cook')
	house.buildBedroom('or maybe just sleep?')

	assert house.kitchen.name == 'let us cook'
	assert house.bedroom.name == 'or maybe just sleep?'
