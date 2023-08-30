from selenium.webdriver.common.by import By

from Xpath import driver

class Carthomepage:
    def __init__(self):
        self.driver = driver

    products = (By.CSS_SELECTOR,"h4[class='product-name']")
    addtocart = (By.XPATH,"//button[@type='button']")
    addbucket = (By.XPATH,"//a[@class='cart-icon']")
    checkout = (By.XPATH,"//button[@type='button']")

    def getProducts(self):
        return self.driver.find_elements(*Carthomepage.products)
    def getAddtoCart(self):
        return self.driver.find_element(*Carthomepage.addtocart)
    def getAddBucket(self):
        return self.driver.find_element(*Carthomepage.addbucket)
    def getCheckout(self):
        return self.driver.find_element(*Carthomepage.checkout)