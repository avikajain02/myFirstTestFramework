from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.mark.usefixtures("setUp")
class TestSampleDemo():

	@pytest.fixture(scope="class")
	def setUp(self):
		global driver
		driver = webdriver.Chrome()
		driver.maximize_window()
		driver.get("https://letskodeit.teachable.com/")
		driver.implicitly_wait(5)
		driver.find_element(By.LINK_TEXT, "Login").click()
		driver.find_element(By.ID, "user_email").send_keys("test@email.com")
		driver.find_element(By.ID, "user_password").send_keys("abcabc")
		driver.find_element(By.NAME, "commit").click()
		yield
		driver.close()
		driver.quit()

	@pytest.mark.run(order=1)
	def test_sampleVerifyLoginSuccess(setUp):
		result = driver.find_element(By.XPATH, "//*[@id='search-courses']")
		if result is not None:
			assert True
		else:
			assert False
		return result

	@pytest.mark.run(order=2)
	def test_sampleVerifyTitle(setUp):
		result = driver.title
		if result == "Let's Kode It":
			assert True
		else:
			assert False
		return result

