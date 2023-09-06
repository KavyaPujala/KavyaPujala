from selenium.webdriver.common.by import By


class OrangeLoginPage:
    def __init__(self, driver):
        self.driver = driver

    username = (By.XPATH,"//input[@name='username']")
    password = (By.XPATH,"//input[@name='password']")
    login = (By.XPATH,"//button[@type='submit']")

    def getUserName(self):
        return self.driver.find_element(*OrangeLoginPage.username)
    def getPassword(self):
        return self.driver.find_element(*OrangeLoginPage.password)
    def getLogin(self):
        return self.driver.find_element(*OrangeLoginPage.login)