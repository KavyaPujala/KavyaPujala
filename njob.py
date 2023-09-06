from selenium.webdriver.common.by import By
class Njob:
    def __init__(self, driver):
        self.driver = driver

    job = (By.XPATH,"//a[contains(@href,'viewJobDetails')]")
    jobtitle = (By.XPATH,"(//div[@class='oxd-select-text--after'])[1]")
    jobcategory = (By.XPATH,"(//div[@class='oxd-select-text--after'])[2]")
    save = (By.XPATH,"//button[@type='submit']")
    neelima = (By.LINK_TEXT,"neelima")

    def getJob(self):
        return self.driver.find_element(*Njob.job)
    def getJobtitle(self):
        return self.driver.find_element(*Njob.jobtitle)
    def getJobcategory(self):
        return self.driver.find_element(*Njob.jobcategory)
    def getSave(self):
        return self.driver.find_element(*Njob.save)
    def getNeelima(self):
        return self.driver.find_element(*Njob.neelima)