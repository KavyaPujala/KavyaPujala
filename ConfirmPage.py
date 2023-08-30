from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self,driver):
        self.driver = driver
    country = (By.ID,"country")
    countryvalue = (By.LINK_TEXT,"India")
    checkbox = (By.XPATH,"//div[contains(@class,'checkbox-primary')]")
    purchase = (By.XPATH,"//input[@value='Purchase']")

    def getCountry(self):
        return self.driver.find_element(*ConfirmPage.country)
    def getCountryValue(self):
        return self.driver.find_element(*ConfirmPage.countryvalue)
    def getCheckBox(self):
        return self.driver.find_element(*ConfirmPage.checkbox)
    def getPurchaseButton(self):
        return self.driver.find_element(*ConfirmPage.purchase)
