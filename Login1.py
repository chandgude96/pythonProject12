import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://automation.credence.in//login")
time.sleep(5)
driver.find_element(By.XPATH,"//input[@id='email']").send_keys("Credence@1test.com")
driver.find_element(By.XPATH,"//input[@id='password']").send_keys("Credence@9656")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(5)

try:
    print("login test is sucess")
except NoSuchElementException:
    print("login fail")