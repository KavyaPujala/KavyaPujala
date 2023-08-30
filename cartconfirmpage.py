from selenium.webdriver.common.by import By


class Cartconfirmpage:
    def __init__(self,driver):
        self.driver = driver
    total = (By.XPATH,"//tbody/tr/td[5]/p")
    compare = (By.CLASS_NAME,"totAmt")

    def getTotal(self):
        return self.driver.find_elements(*Cartconfirmpage.total)