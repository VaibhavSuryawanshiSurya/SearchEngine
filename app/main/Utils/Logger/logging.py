import logging

class Logger:

	 def __init__(self):

	 	format = logging.Formatter('%(asctime)s : %(name)s : %(levelname)s : %(message)s')

	 	#Create Debug logger
	 	debug_logger = logging.getLogger('debug')
	 	debug_logger.setLevel(logging.DEBUG)

	 	debug_file = logging.FileHandler('app/main/Utils/Logger/debuglog.log')
	 	debug_file.setFormatter(format)

	 	debug_logger.addHandler(debug_file)
	 	self.debug_logger = debug_logger


	 	#Create Info logger
	 	info_logger = logging.getLogger('info')
	 	info_logger.setLevel(logging.INFO)

	 	info_file = logging.FileHandler('app/main/Utils/Logger/infolog.log')
	 	info_file.setFormatter(format)

	 	info_logger.addHandler(info_file)
	 	self.info_logger = info_logger


	 	#Create Error logger
	 	error_logger = logging.getLogger('error')
	 	error_logger.setLevel(logging.ERROR)

	 	error_file = logging.FileHandler('app/main/Utils/Logger/errorlog.log')
	 	error_file.setFormatter(format)

	 	error_logger.addHandler(error_file)

	 	self.error_logger = error_logger