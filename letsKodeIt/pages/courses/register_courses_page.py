import utilities.custom_logger as cl
import logging
from base.base_page import BasePage

class RegisterCoursePage(BasePage):
	log = cl.customLogger(logging.DEBUG)
	def __init__(self,driver):
		super().__init__(driver)
		self.driver = driver

	#locators:
	_search_box = "search-courses"
	_search_button = "search-course-button"
	_course = "//div[contains(text(),'JavaScript for beginners')]"
	_enroll_button = "//*[@id='enroll-button-top']"
	_iframe_locator1 = "//iframe[contains(@name,'__privateStripeFrame8')]"
	_iframe_locator2 = "//iframe[contains(@name,'__privateStripeFrame9')]"
	_iframe_locator3 = "//iframe[contains(@name,'__privateStripeFrame10')]"
	_iframe_locator4 = "//iframe[contains(@name,'__privateStripeFrame11')]"
	_cc_postal = "//input[@name='postal']"
	_cc_num = "//input[@name='cardnumber']"
	_cc_exp = "//input[@name='exp-date']"
	_cc_cvv = "//input[@name='cvc']"
	_terms_agree_checkbox = "//input[@id='agreed_to_terms_checkbox']"
	_submit_enroll = "//button[@id='confirm-purchase']"

	def enterCourseName(self,courseName):
		self.sendKeys(courseName,self._search_box)
		self.elementClick(self._search_button)

	def selectCourseToEnroll(self, fullCourseName):
		self.elementClick(self._course, locatorType="xpath")

	def enrollCourse(self,num="", exp="", cvv="", postal=""):
		self.elementClick(self._enroll_button, locatorType="xpath")
		self.switchToIFrame(self._iframe_locator1, locatorType="xpath")
		self.scrollViewElement(self._cc_num, locatorType="xpath")
		self.sendKeys(num, self._cc_num, locatorType="xpath")
		self.switchToDefault()
		self.switchToIFrame(self._iframe_locator2, locatorType="xpath")
		self.sendKeys(exp, self._cc_exp, locatorType="xpath")
		self.switchToDefault()
		self.switchToIFrame(self._iframe_locator3, locatorType="xpath")
		self.sendKeys(cvv, self._cc_cvv, locatorType="xpath")
		self.switchToDefault()
		self.switchToIFrame(self._iframe_locator4, locatorType="xpath")
		self.sendKeys(postal, self._cc_postal, locatorType="xpath")
		self.switchToDefault()

	def verifyEnrollButtonEnabled(self):
		self.elementClick(self._terms_agree_checkbox,locatorType="xpath") # this will check the terms agree check box
		result = self.isElementEnabled(self._submit_enroll, locatorType="xpath")
		return result












