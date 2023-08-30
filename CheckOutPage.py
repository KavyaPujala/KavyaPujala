from selenium.webdriver.common.by import By


class CheckOutPage:
    checkout = (By.CSS_SELECTOR,"a[class*='btn-primary']")
    checkoutItems = (By.XPATH,"//h4[@class='card-title']")
    addtocart = (By.CSS_SELECTOR,"div[class='card-footer']")
    checkout2 = (By.CSS_SELECTOR,"button[class*='btn-success']")


    def getCheckOutButton(self):
        return self.driver.find_element(*CheckOutPage.checkout)
    def getCheckOutItems(self):
        return self.driver.find_element(*CheckOutPage.checkoutItems)
    def AddToCart(self):
        return self.driver.find_element(*CheckOutPage.addtocart)
    def getFinalCheckOut(self):
        return self.driver.find_element(*CheckOutPage.checkout2)