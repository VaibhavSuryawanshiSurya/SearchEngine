try:
	import concurrent.futures
	from app.main.Utils.Logger.logging import *
	from app.main.Controller.Search.SearchInDrive import *
	from app.main.Business.Search.SearchParallelProcesingAbstract import *

except Exception as e:
    print(e,'\n')


class Parallel(Processing):

	def multiProcessing(self,filename,SystemDrives):

		with concurrent.futures.ProcessPoolExecutor() as excutor:
			path = [excutor.submit(findFiles,filename,i).result() for i in SystemDrives]

			logger_module.debug_logger.debug(f'Result path generated by after search in drives {path} ')

			return path 

def main():
	pass

if __name__ == '__main__':
	main()