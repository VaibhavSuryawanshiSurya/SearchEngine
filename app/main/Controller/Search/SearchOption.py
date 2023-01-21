try:
	from app.main.Utils.Logger.logging import *
	from app.main.Controller.Root.ActiveRootFinder import *
	from app.main.Repository.Search.SearchDbOperation import *
	from app.main.Controller.Root.ExtensionRootRemove import *
	from app.main.Business.Search.SearchOptionAbstract import *
	from app.main.Controller.Search.SearchParallelProcessing import *

except Exception as e:
    print(e,'\n')

# Creat object of Logger class
logger_module = Logger()


class SearchType(SearchOptions):

	def sreachDB(self, filename, drive):
		
		# Database module class
		DB = DbOperation()

		result = DB.searchResultPath(filename, drive)
		# print(len(result))
		if len(result) ==0:
			logger_module.info_logger.info('Result not found in Database')
			return 'NO'

		print("\nAvailable Path:\n")
		for r in result:
			print(r)

		print('\nResult Found in DataBase')

		logger_module.debug_logger.debug(f'Search result for {filename} file in Database {result}')
		logger_module.info_logger.info('Result found in Database')


	def searchDrive(self, filename, SystemDrives):

		DB = DbOperation()
		P = Parallel()

		# Calling Multi Processing function 
		path = P.multiProcessing(filename,SystemDrives)

		if not ''.join(path):
			print(f"{filename} file does not fond in the System")

			logger_module.info_logger.info(f"{filename} file does not fond in the System")
		
		else:
			ER = ExtensionRemove()
			print("\nAvailable Path:\n")
			for p in path:
				if p != '':
					for path in p.split('\n'):
						filename = ER.selectFileNameFromPath(path)
						DB.insertInputPath(filename,path)
						print(path)
			print('\nResult found in Drive')
			
			logger_module.info_logger.info('Result found in Drive')