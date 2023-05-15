from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Edge()
driver.get('https://github.com/login')
mail=driver.find_element(By.ID,"login_field").send_keys("Your User Name Here")
password = driver.find_element(By.ID,"password").send_keys("Your Password here")
login = driver.find_element(By.NAME,'commit').click()
