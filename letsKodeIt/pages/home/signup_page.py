import utilities.custom_logger as cl
from base.base_page import BasePage
import logging

class SignupPage(BasePage):

	log = cl.customLogger((logging.DEBUG))

	def __init__(self, driver):
		super().__init__(driver)
		self.driver = driver

	# Locators:
	_signup_link = "header-sign-up-btn"
	_name = "user_name"
	_email = "user_email"
	_password = "user_password"
	_confirm_password = "user_password_confirmation"
	_captcha = "recaptcha-anchor"
	_notify_checkbox = "user_unsubscribe_from_marketing_emails"
	_terms_agree_checkbox = "user_agreed_to_terms"
	_signup_button = "commit"

	def clickSignupButton(self):
		self.elementClick(self._signup_link)

	def enterSignupDetails(self,name, email, password):
		self.sendKeys(name, self._name)
		self.sendKeys(email, self._email)
		self.sendKeys(password, self._password)
		self.sendKeys(password, self._confirm_password)

	def finalClicks(self):
		self.elementClick(self._captcha)
		self.elementClick(self._notify_checkbox)
		self.elementClick(self._terms_agree_checkbox)
		self.elementClick(self._signup_button, locatorType="name")

