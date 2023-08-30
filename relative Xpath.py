from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver= webdriver.Chrome()
driver.get("https://www.google.co.in/")
time.sleep(5)
driver.maximize_window()
#driver.find_element(By.XPATH,"//a[@aria-label='Gmail (opens a new tab)']").click()
#driver.find_element(By.XPATH,"//a[contains(@href,'mail')]").click()


