from selenium.webdriver.common.by import By
class nhome:
    def __init__(self, driver):
        self.driver = driver

    pim = (By.CSS_SELECTOR,"a[href*='Pim']")
    addemployee = (By.XPATH,"(//a[contains(@href,'#')]) [2]")
    firstname = (By.XPATH,"//input[@name='firstName']")
    lastname = (By.XPATH,"//input[@name='lastName']")
    employeeid = (By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[2]")
    profile = (By.XPATH,"//img[@class='employee-image']")
    switch = (By.XPATH,"//span[contains(@class,'oxd-switch-input')] ")
    username = (By.XPATH,"(//input[@autocomplete='off']) [1]")
    enable = (By.XPATH,"(//span[contains(@class,'radio-input')] )[1]")
    password = (By.XPATH,"(//input[@type='password'])[1]")
    confirmpassword = (By.XPATH,"(//input[@type='password'])[2]")
    save = (By.XPATH,"//button[@type='submit']")

    def getPim(self):
        return self.driver.find_element(*nhome.pim)
    def getAddemployee(self):
        return self.driver.find_element(*nhome.addemployee)
    def getFirstname(self):
        return self.driver.find_element(*nhome.firstname)
    def getLastname(self):
        return self.driver.find_element(*nhome.lastname)
    def getEmployeeid(self):
        return self.driver.find_element(*nhome.employeeid)
    def getProfile(self):
        return self.driver.find_element(*nhome.profile)
    def getSwitch(self):
        return self.driver.find_element(*nhome.switch)
    def getUsername(self):
        return self.driver.find_element(*nhome.username)
    def getEnable(self):
        return self.driver.find_element(*nhome.enable)
    def getPassword(self):
        return self.driver.find_element(*nhome.password)
    def getConfirmpassword(self):
        return self.driver.find_element(*nhome.confirmpassword)
    def getSave(self):
        return self.driver.find_element(*nhome.save)