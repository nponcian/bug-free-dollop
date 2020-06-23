class EngineFactory(object):
	def create(self, model):
		self.name = 'real'
		return self

class Car(object):
	def __init__(self, details):
		self.model = self.readEngineModel(details)
		self.engine = EngineFactory().create(self.model);

	def readEngineModel(self, details):
		return details['model']

def test_car_engine():
	# TODO test car with fake engine
	# assert car.engine.name == 'fake'