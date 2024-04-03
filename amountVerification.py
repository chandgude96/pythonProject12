import time

from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.common import NoSuchElementException


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://automation.credence.in//login")

driver.find_element(By.XPATH,"//input[@id='email']").send_keys("Credence@1test.com")
driver.find_element(By.XPATH,"//input[@id='password']").send_keys("Credence@9656")
driver.find_element(By.XPATH, "//button[@type='submit']").click()


##click on product
driver.find_element(By.XPATH,"//img[@src='https://automation.credence.in/img/xbox-one.jpg']").click()
### add to cart
driver.find_element(By.XPATH,"//input[@value='Add to Cart']").click()
driver.implicitly_wait(2)
product_quantity=Select(driver.find_element(By.XPATH,"//select[@class='quantity']")) ##Captital S
product_quantity.select_by_index(1)         #### small s
driver.find_element(By.XPATH,"//a[@class='btn btn-success btn-lg']").click()

driver.implicitly_wait(2)
