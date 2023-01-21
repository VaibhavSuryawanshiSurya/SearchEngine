from app.main.UI.SearchForm import *
from app.main.Utils.Logger.logging import *
  
# Creat object of Logger class
logger_module = Logger()

class ViweLogger:

	def chooseLogger(self):
		
		while True:

			User_Input = Inputs()
			choice = User_Input.loggerChoice()

			if choice == 1:
				logger_module.info_logger.info('User choose Info logger file')
				
				print("INFO LOGGER:")
				filenamePath = 'app/main/Utils/Logger/infolog.log'
				ViweLogger.fileReader(filenamePath)
				return

			elif choice == 2:
				logger_module.info_logger.info('User choose Debug logger file')
				
				print("DEBUG LOGGER:")
				filenamePath = 'app/main/Utils/Logger/debuglog.log'
				ViweLogger.fileReader(filenamePath)
				return

			elif choice == 3:
				logger_module.info_logger.info('User choose Error logger file')
				
				print("ERROR LOGGER:")
				filenamePath = 'app/main/Utils/Logger/errorlog.log'
				ViweLogger.fileReader(filenamePath)
				return

			elif choice == 4:
				logger_module.info_logger.info('User choose All logger file')

				print("INFO LOGGER:")
				filenamePath = 'app/main/Utils/Logger/infolog.log'
				ViweLogger.fileReader(filenamePath)

				print("DEBUG LOGGER:")
				filenamePath = 'app/main/Utils/Logger/debuglog.log'
				ViweLogger.fileReader(filenamePath)

				print("ERROR LOGGER:")
				filenamePath = 'app/main/Utils/Logger/errorlog.log'
				ViweLogger.fileReader(filenamePath)
				
				return

			else:
				logger_module.info_logger.info('User choose Invalid logger file')

				print("Invalid Input\nTry Again!")


	def fileReader(filenamePath):

		file = open(filenamePath, 'r')

		for line in file:
			print(line)

		file.close()