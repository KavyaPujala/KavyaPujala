from selenium.webdriver.chrome import webdriver
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
checkbox = driver.find_element(By.XPATH,"//input[@type='checkbox']")

op2 = driver.find_element(By.ID,"checkBoxOption2")
op2.click()
time.sleep(5)
assert op2.is_selected()
op3=driver.find_element(By.ID,"checkBoxOption3")
op3.click()

