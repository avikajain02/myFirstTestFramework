import logging

class loggerDemoConsole():

	def testLog(self):
		# create logger
		logger = logging.getLogger(loggerDemoConsole.__name__)
		logger.setLevel(logging.INFO)

		# create console handler and set level to info. this will give output on console
		chandler = logging.StreamHandler()
		chandler.setLevel(logging.INFO)

		# create formatter
		formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')

		# add formatter to console handler -> ch
		chandler.setFormatter(formatter)

		#add console handler to logger
		logger.addHandler(chandler)

		# logging messages:
		logger.debug("debug message")
		logger.info("info message")
		logger.warning("warning message")
		logger.error("error message")
		logger.critical("crtical message")

demo = loggerDemoConsole()
demo.testLog()