try:
	from app.main.UI.SearchForm import *
	from app.main.Utils.Logger.logging import *
	from app.main.Utils.Logger.Viewlogger import *
	from app.main.Controller.Search.SearchOption import *
	from app.main.Controller.Root.ActiveRootFinder import *
	from app.main.Controller.Search.SearchUserLogin import *
	from app.main.Repository.Search.SearchDbOperation import *
	from app.main.Repository.Analytics.TransactionModule import *
	from app.main.Controller.Search.SearchParallelProcessing import *

except Exception as e:
    print(e,'\n')

# Creat object of Logger class
logger_module = Logger()


class SearchEngine:

	def __init__(self):
		self.filename = None


	def acceptFileName(self):
		
		User_Input = Inputs()
		self.filename = User_Input.userInputFileNameS()

		TM = DbTransaction()
		TM.insertTransactions('Search' ,self.filename)
		
		logger_module.info_logger.info('Accept file name for Search Succesfully')


	def viewDrives(self):
		
		AR = ActiveRoot()
		self.system_drive = AR.activeRootFinder()
		
		print("\nDrive present in the system:-")
		
		for i in range(len(self.system_drive)):
			print(f'{i+1}.{self.system_drive[i]}',end = '\t')
			
	
	def userCredentials(self):

		while True:

			User_Input = Inputs()
			choice = User_Input.signUpOption()


			if choice == 1:
				logger_module.info_logger.info('User trying to Login')

				User_Input = Inputs()
				self.user_name, self.password = User_Input.loginInfo()

				UL = UserLogin()
				validate = UL.checkLogiInfo(self.user_name, self.password)
				
				return validate

			elif choice == 2:
				logger_module.info_logger.info('User trying to SignUp')
				
				DB = DbOperation()

				User_Input = Inputs()
				user_name, password = User_Input.loginInfo()

				DB.insertUserInfo(user_name, password)
				print("User create Succesfully")

				logger_module.info_logger.info('User create Succesfully')

				return True

			else:
				Print("Invalid Chooise\nTry Agai!")
				logger_module.info_logger.info('User give invalid chooise userCredentials function ')

 
	def chooseDrive(self):

		print("\nChoose Drive(s) to search file:-")
		
		for i in range(len(self.system_drive)):
			print(f'{i+1}.{self.system_drive[i]}',end = '\t')
		
		print(f'{i+2}. All')

		User_Drive = Inputs()
		self.drive_choose = User_Drive.userInputDrive(self.system_drive)

		ST = SearchType()
		P = Parallel()
		
		if self.drive_choose == len(self.system_drive)+1:
			
			db_result = ST.sreachDB(self.filename,self.system_drive)

			if db_result == 'NO':		
				ST.searchDrive(self.filename,self.system_drive)
			
			logger_module.info_logger.info('User select all drive to search file ')

		else :
			
			db_result = ST.sreachDB(self.filename, [self.system_drive[self.drive_choose-1]])

			if db_result == 'NO':		
				ST.searchDrive(self.filename,[self.system_drive[self.drive_choose-1]])

			logger_module.info_logger.info(f'User select {self.system_drive[self.drive_choose-1]} drive to search file ')


	def deleteFromDatabase(self):

		User_Input = Inputs()
		self.filename = User_Input.userInputFileNameD()
		
		logger_module.info_logger.info('Accept file name for Delete file from database Succesfully!')

		DB = DbOperation()
		DB.deletePath(self.filename)

		#Insert Transaction in Database
		TM = DbTransaction()
		TM.insertTransactions('Delete' ,self.filename)

		logger_module.info_logger.info('User Delete filename Succesfully')


	def errorLogger(self):

		VL = ViweLogger()
		VL.chooseLogger()


	def viewTransaction(self):

		TM = DbTransaction()

		User_Input = Inputs()
		choice = User_Input.chooseTransactionHistory()

		if choice == 1:

			TM.getAllTransactions()
			logger_module.info_logger.info('User select All Transaction History')

		elif choice == 2:

			User_Input = Inputs()
			start_date, end_date = User_Input.datephrase()

			TM.getTransactionBetweenDates(start_date, end_date)
			logger_module.info_logger.info('User select Transaction History between Date')


def main():

	search_engine = SearchEngine()
	
	while True:

		validate = search_engine.userCredentials()
		
		if validate:
			logger_module.info_logger.info('User Login Succesfully')

			while True:

				User_Input = Inputs()
				choice = User_Input.operations()
				
				if choice == 1:

					search_engine.viewDrives()
					search_engine.acceptFileName()
					search_engine.chooseDrive()

					logger_module.info_logger.info('User select Search function')

				elif choice == 2:

					search_engine.deleteFromDatabase()

					logger_module.info_logger.info('User select Delete function')

				elif choice == 3:
					
					search_engine.viewTransaction()
					
					logger_module.info_logger.info('User select Transaction History function')

				elif choice == 4:
					
					search_engine.errorLogger()
					
					logger_module.info_logger.info('User select Error Logger function')

				elif choice == 5:
					# Log out user
					logger_module.info_logger.info('User Log Out Succesfully')
					validate = None
					
					break

		else:
			logger_module.info_logger.info('Invalid User info')
			print("Invalid User\nTry Again!")


if __name__ == '__main__':
	main()