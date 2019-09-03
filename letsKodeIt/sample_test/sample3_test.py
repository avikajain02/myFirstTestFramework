import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://letskodeit.teachable.com/")
driver.implicitly_wait(5)
driver.find_element_by_id("header-sign-up-btn").click()
driver.find_element_by_id("user_name").send_keys("")
driver.find_element_by_id("user_email").send_keys("")
driver.find_element_by_id("user_password").send_keys("abc")
driver.find_element_by_id("user_password_confirmation").send_keys("ancbk")
element = driver.find_element_by_xpath("//iframe[@name='a-e50k8stpn2tv']")
driver.switch_to.frame(element)
driver.find_element_by_id("recaptcha-anchor").click()
driver.switch_to_default.content()
driver.find_element_by_id("user_unsubscribe_from_marketing_emails").click()
driver.find_element_by_id("user_agreed_to_terms").click()
driver.find_element_by_name("commit").click()
error_msg = driver.find_element_by_xpath("//div/ul/li[contains(text(),'Email is required')]")
if error_msg is not None:
	print("error verified")
else:
	print("error not verified")



