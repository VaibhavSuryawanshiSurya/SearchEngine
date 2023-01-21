from abc import ABC, abstractmethod


class Extention(ABC):

	@abstractmethod
	def inputFileNameExtensionRemove(self):
		pass

	@abstractmethod
	def selectFileNameFromPath(self):
		pass
