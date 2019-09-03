from selenium import webdriver
import pytest
import time

# to generate html reports via pytest run:  pytest -v -s --html=report.html "file name"
# to create customaised reports add --self-contained-html after --html=report.html

@pytest.fixture()
def test_setup():
	global driver
	chrome_options = webdriver.ChromeOptions()
	prefs = {"profile.default_content_setting_values.notifications": 2}
	chrome_options.add_experimental_option("prefs", prefs)
	driver = webdriver.Chrome(options=chrome_options)
	driver.implicitly_wait(10)
	driver.maximize_window()

	driver.get("https://www.facebook.com")
	driver.find_element_by_id("email").send_keys("avikajain0206@gmail.com")
	driver.find_element_by_id("pass").send_keys("avikatestadmin")
	driver.find_element_by_id("loginbutton").click()
	print("Login successful")
	time.sleep(10)

	yield

	driver.find_element_by_xpath("//*[@id='logoutMenu']//a").click()
	driver.find_element_by_xpath("//div[@id='BLUE_BAR_ID_DO_NOT_USE']//li[8]").click()
	print("Logout Successful")
	#driver.close()
	driver.quit()
	print("test completed")


def test_login(test_setup):

	x = driver.title
	print(x)
	time.sleep(5)
	assert x == "Facebook"
	print(x)
	time.sleep(5)

def test_updateStatus(test_setup):

	driver.find_element_by_xpath("//*[@name='xhpc_message']").send_keys("Hello World")
	print("Typed the status")
	time.sleep(10)
	driver.find_element_by_xpath("//*[@data-testid='media-sprout']").send_keys("C:/Users/Public/Pictures/Sample Pictures/Tulips.jpg")
	time.sleep(5)
	print("Uploaded the photo")
	driver.find_element_by_xpath("//*[@data-testid='react-composer-post-button']").click()
	print("Uploaded status and pic successfully")
	time.sleep(10)











