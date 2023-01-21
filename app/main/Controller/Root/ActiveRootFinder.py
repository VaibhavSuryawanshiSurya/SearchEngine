try:
	import os
	from app.main.Business.Root.RootAbstract import *
	from app.main.Utils.Logger.logging import *
	
	# Creat object of Logger class
	logger_module = Logger()
except Exception as e:
    print(e,'\n')



class ActiveRoot(Root):

	def __init__(self):
		self.system_drive = None

	def activeRootFinder(self):
		self.system_drive = [ chr(x) + ":" for x in range(65,91) if os.path.exists(chr(x) + ":") ]
		# print(f'System contain {len(self.system_drive)} Active Drive(s)',self.system_drive)
		
		logger_module.debug_logger.debug(f'System contains {self.system_drive} drives')

		return self.system_drive


def main():

	AR = ActiveRoot()
	print(AR.activeRootFinder())

if __name__ == '__main__':
	main()