import logging
import logging.config

class loggerDemoConf():

	def testLog(self):
		# create logger
		logging.config.fileConfig('logging.conf')
		logger = logging.getLogger(loggerDemoConf.__name__)

		# logging messages:
		logger.debug("debug message")
		logger.info("info message")
		logger.warning("warning message")
		logger.error("error message")
		logger.critical("crtical message")

demo = loggerDemoConf()
demo.testLog()



