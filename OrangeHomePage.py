from selenium.webdriver.common.by import By

class OrangeHomePage:
    def __init__(self, driver):
        self.driver = driver

    recruitment = (By.XPATH, "//a[contains(@href,'Recruitment')]")
    canditates = (By.XPATH,"//a[contains(@href,'#')]")
    type = (By.XPATH, "//div[contains(@class,'oxd-autocomplete')]/input")
    mohan = (By.XPATH,"//div[@role='option']")
    compare = (By.XPATH,"//div[text()='mohan  k']")
    search = (By.XPATH, "//button[@type='submit']")
    reset = (By.XPATH, "//button[@type='reset']")

    def getRecruitment(self):
        return self.driver.find_element(*OrangeHomePage.recruitment)
    def getCanditates(self):
        return self.driver.find_element(*OrangeHomePage.canditates)
    def getMohan(self):
        return self.driver.find_element(*OrangeHomePage.mohan)

    def getType(self):
        return self.driver.find_element(*OrangeHomePage.type)
    def getCompare(self):
        return self.driver.find_element(*OrangeHomePage.compare)

    def getSearch(self):
        return self.driver.find_element(*OrangeHomePage.search)

    def getReset(self):
        return self.driver.find_element(*OrangeHomePage.reset)