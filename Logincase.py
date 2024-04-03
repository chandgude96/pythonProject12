#registration case
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException
driver = webdriver.Chrome()
driver.get("https://automation.credence.in//register")
time.sleep(5)
driver.maximize_window()

#
driver.find_element(By.ID,"name").send_keys("Credence")
driver.find_element(By.ID,"email").send_keys("Credence@3test.com")
driver.find_element(By.ID,"password").send_keys("Credence@9656")
driver.find_element(By.ID,"password-confirm").send_keys("Credence@9656")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

time.sleep(5)
try:
    driver.find_element(By.XPATH,"//h2[normalize-space()='CredKart']")
    print("registration Pass")
except NoSuchElementException:
    print("registration case fail")





