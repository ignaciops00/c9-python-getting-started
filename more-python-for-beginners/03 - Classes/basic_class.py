class Presenter():
	def __init__(self, name):
		# Constructor
		self.name = name
  
	def say_hello(self):
		# method
		print('Hello, ' + self.name)

presenter = Presenter('Nacho')
#presenter.name = 'Christopher'
presenter.say_hello()