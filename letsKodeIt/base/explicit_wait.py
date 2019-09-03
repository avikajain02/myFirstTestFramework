from traceback import print_stack
from base.selenium_driver import SeleniumDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


class ExplicitWaitType():

	def __init__(self, driver):
		self.driver = driver
		self.seldr = SeleniumDriver(driver)

	def waitForElement(self, locator, locatorType="id",
					   timeout=10, pollFrequency=0.5):
		element = None
		try:
			byType = self.seldr.getByType(locatorType)
			print("Waiting for maximum :: " + str(timeout) +
				  ":: seconds for elemnt to be clickable")
			wait = WebDriverWait(self.driver, 10, pollFrequency=1,
								 ignored_exceptions=[NoSuchElementException,
													 ElementNotVisibleException,
													 ElementNotSelectableException])
			element = wait.until(EC.element_to_be_clickable(byType, locator))
			print("Element appeared on the web page")

		except:
			print("Element not appeared on the web page")
			print_stack()
		return element