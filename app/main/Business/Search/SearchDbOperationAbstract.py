from abc import ABC, abstractmethod


class Database(ABC):

	@abstractmethod
	def createTable(self):
		pass

	@abstractmethod
	def insertInputPath(self):
		pass

	@abstractmethod
	def deleteDuplicateRow(self):
		pass

	@abstractmethod
	def searchResultPath(self):
		pass

	@abstractmethod
	def deletePath(self):
		pass

	@abstractmethod
	def insertUserInfo(self):
		pass

	@abstractmethod
	def searchUserInfo(self):
		pass
