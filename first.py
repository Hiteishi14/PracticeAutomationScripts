import time
from selenium import webdriver
#from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get(r'https://practicetestautomation.com/practice-test-login/')
driver.maximize_window()
time.sleep(3)
driver.find_element('id','username').send_keys('student')
#driver.find_element('name','username').send_keys('student')
driver.find_element('id','password').send_keys('Password123')
#driver.find_element('name','password').send_keys('Password123')
driver.find_element('class name','btn').click()
time.sleep(3)
#links = driver.find_element(By.LINK_TEXT,'Home')
#links.click()
driver.find_element('link text','Practice Test Automation.').click()
print(len(driver.find_elements('tag name','a')))
time.sleep(5)
