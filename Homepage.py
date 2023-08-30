from selenium.webdriver.common.by import By





class Homepage:
    def __init__(self,driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.XPATH, "//label[text()='Name']/following-sibling::input")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkbox = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    button = (By.ID, "inlineRadio2")
    date = (By.NAME, "bday")
    submit = (By.XPATH, "//input[@type='submit']")
    success = (By.XPATH, "//div[contains(@class,'alert')]")

    def shopItem(self):
        return self.driver.find_element(*Homepage.shop)

    def getName(self):
        return self.driver.find_element(*Homepage.name)

    def getEmail(self):
        return self.driver.find_element(*Homepage.email)

    def getPassword(self):
        return self.driver.find_element(*Homepage.password)

    def getCheckbox(self):
        return self.driver.find_element(*Homepage.checkbox)

    def getGender(self):
        return self.driver.find_element(*Homepage.gender)

    def getButton(self):
        return self.driver.find_element(*Homepage.button)

    def getDate(self):
        return self.driver.find_element(*Homepage.date)

    def Submit(self):
        return self.driver.find_element(*Homepage.submit)

    def getSuccess(self):
        return self.driver.find_element(*Homepage.success)
