try:
	import base64
	from app.main.Exception.Search.FileNameException import *
	from app.main.Exception.Root.InvalidChoiceException import *
	from app.main.Controller.Root.ExtensionRootRemove import *
	from app.main.Exception.Search.EmailIDException import *
	from app.main.Utils.Logger.logging import *

except Exception as e:
    print(e,'\n')


# Creat object of Logger class
logger_module = Logger()


class Inputs:

	def __init__(self):
		pass


	def userInputFileNameS(self):

		while True:
			
			try:
				filename = input('\n\nEnter File Name: ')
				validateInput(filename)

				ER = ExtensionRemove() 

				self.filename = ER.inputFileNameExtensionRemove(filename)
				return self.filename

			except InvalidInputError as e:
				logger_module.error_logger.error('Exception Occured', exc_info=True)
				print(e)


	def userInputFileNameD(self):

		while True:
			try:
				filename = input('\nEnter File Name: ')
				validateInput(filename)

				return filename

			except InvalidInputError as e:
				logger_module.error_logger.error('Exception Occured', exc_info=True)
				print(e)


	def userInputDrive(self,system_drive):

		while True:
			
			try:
				self.drive_choose = int(input('Choose the Drive: '))
				
				validateDrive(self.drive_choose,len(system_drive))
				
				return self.drive_choose

			except InvalidInputError as e:
				logger_module.error_logger.error('Exception Occured', exc_info=True)
				print(e)


	def loginInfo(self):

		while True:

			try:
				user_name = input("\nEnter your Email I'd as user name:\t").lower()
				
				validateUserName(user_name)
				
				password = input("\nEnter Password:\t").encode("utf-8")
				encoded_password = str(base64.b64encode(password))[2:-1] #Password encryption 

				return user_name, encoded_password

			except InvalidEmailIDError as e:
				logger_module.error_logger.error('Exception Occured', exc_info=True)
				print(e)


	def operations(self):

		while True:

			print("\nOperatons: \n1. Search File \n2. Dlete File \n3. View Transaction History \n4. View Error Logger \n5. Log Out")
			choice = int(input(f"\nChoose the option :\t"))
			
			if choice > 0 and choice <= 5:
				return choice
			
			else:
				logger_module.info_logger.info('User give invalid chooise at the time of operation select')
				
				print("Invalid Chooise\nTry Agai!")


	def loggerChoice(self):

		print("1. Info logger \n2. Debug Logger \n3. Error Logger \n4. All")
		choice = int(input(f"\nChoose the option :\t"))
		
		return choice


	def signUpOption(self):
		print("\n1. Login\t 2. SignUp")
		choice = int(input("Enter your choice :\t"))
		
		return choice


	def chooseTransactionHistory(self):

		while True:

			print("\nTransaction Oprions: \n1. Get All Transactions\t 2. Get Transaction Between Dates")
			choice = int(input("Enter Transaction choice:\t"))
			
			if choice > 0 and choice <= 3:
				return choice
			else:
				print("Invalid Chooise\nTry Agai!")


	def datephrase(self):

		start_date = input("Enter start date in form YYYY-MM-DD :\t")
		end_date = input("Enter end date in form YYYY-MM-DD :\t")

		return start_date,end_date


def main():
	inputs = Inputs()

if __name__ == '__main__':
	main()