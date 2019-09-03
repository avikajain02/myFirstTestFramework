from pages.courses.register_courses_page import RegisterCoursePage
from pages.home.login_page import LoginPage
from utilities.test_status import TestStatus
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class RegisterCoursesTests(unittest.TestCase):

	@pytest.fixture(autouse=True)
	def classSetUp(self, oneTimeSetUp):
		self.courses = RegisterCoursePage(self.driver)
		self.ts = TestStatus(self.driver)
		self.lp = LoginPage(self.driver)

	@pytest.mark(order=1)
	def test_enrollmentButtonEnabled(self):
		self.lp.login("test@email.com", "abcabc")
		self.courses.enterCourseName("JavaScript")
		self.courses.selectCourseToEnroll("JavaScript for beginners")
		self.courses.enrollCourse("2344121212121212","0411","332","133201")
		result1 = self.courses.verifyEnrollButtonEnabled()
		self.ts.markFinal("test_enrollmentButtonEnabled",result1, "Enrollement Button Disabled")
