class EngineFactory(object):
	@classmethod
	def create(cls, model, name='real'):
		cls_instance = cls()
		cls_instance.model = model
		cls_instance.name = name
		return cls_instance

	@classmethod
	def createFromDetails(cls, details):
		cls_instance = cls()
		cls_instance.model = details['model']
		cls_instance.name = details['name']
		return cls_instance

class Car(object):
	def __init__(self, details):
		engineModel = self.readEngineModel(details)
		engineName = self.readEngineName(details)
		self.engine = EngineFactory.create(engineModel, engineName);

	def readEngineModel(self, details):
		return details['model']

	def readEngineName(self, details):
		return details['name']

class CarUpdated(object):
	def __init__(self, engine):
		self.engine = engine

def test_car_engine():
	# TODO test car with fake engine

	details = {
		'model': 'Corolla',
		'name': 'fake'
	}

	car = Car(details)
	assert car.engine.name == 'fake'

	engine = EngineFactory.createFromDetails(details)
	carUpdated = CarUpdated(engine)
	assert carUpdated.engine.name == 'fake'
