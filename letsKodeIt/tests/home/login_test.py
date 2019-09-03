from pages.home.login_page import LoginPage
import unittest
import pytest
from utilities.test_status import TestStatus

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

	@pytest.fixture(autouse=True)
	def classSetup(self, oneTimeSetUp):
		self.lp = LoginPage(self.driver)
		self.ts = TestStatus(self.driver)

	@pytest.mark.run(order=2)
	def test_validLogin(self):
		self.lp.login("test@email.com", "abcabc")
		result1 = self.lp.verifyLoginTitle()
		self.ts.mark(result1, "Title Verification")
		result2 = self.lp.verifyLoginSuccessful()
		self.ts.markFinal("test_validLogin", result2, "Login Verification")

	@pytest.mark.run(order=1)
	def test_invalidLogin(self):
		self.lp.login("tst@email.com", "abcabcabc")
		result = self.lp.verifyLoginFailed()
		self.ts.mark(result, "Login not Successful")