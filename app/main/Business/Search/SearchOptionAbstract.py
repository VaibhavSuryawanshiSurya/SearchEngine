from abc import ABC, abstractmethod

class SearchOptions(ABC):

	@abstractmethod
	def sreachDB(self):
		pass

	@abstractmethod
	def searchDrive(self):
		pass