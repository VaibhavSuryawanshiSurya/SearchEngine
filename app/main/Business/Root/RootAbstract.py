from abc import ABC, abstractmethod

class Root():

	@abstractmethod
	def activeRootFinder(self):
		pass

	@abstractmethod
	def systemRootFinder(self):
		pass