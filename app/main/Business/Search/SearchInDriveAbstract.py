from abc import ABC, abstractmethod


class SearchAbstract(ABC):

	@abstractmethod
	def createNewIindex(self):
		pass


	@abstractmethod
	def search(self):
		pass
