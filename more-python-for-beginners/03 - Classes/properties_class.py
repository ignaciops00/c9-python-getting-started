class Presenter():
	def __init__(self, name):
		# Constructor
		self.name3 = name

	@property
	def name3(self):
		print('Retrieving name...')
		return self.__name
	@name3.setter
	def name3(self, value):
		# cool validation here
		print('Validating name...')
		self.__name = value

presenter = Presenter('Chris')
presenter.name3 = 'Christopher'
print(presenter.name3)