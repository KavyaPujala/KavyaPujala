from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver= webdriver.Chrome()
driver.get("https://www.facebook.com/")
time.sleep(5)
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,"input[class='inputtext _55r1 _6luy']").send_keys("sandhya")
time.sleep(5)