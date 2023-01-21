from abc import ABC, abstractmethod


class Transaction(ABC):

	@abstractmethod
	def getAllTransactions(self):
		pass

	@abstractmethod
	def getTransactionBetweenDates(self):
		pass