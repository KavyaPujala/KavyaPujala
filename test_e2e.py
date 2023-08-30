import pytest
import time
from selenium.webdriver.support.select import Select
from pageobjects.CheckOutPage import CheckOutPage
from pageobjects.ConfirmPage import ConfirmPage
from pageobjects.Homepage import Homepage




@pytest.mark.usefixtures("setup")
class TestOne:

    def teste2e(self):
        homepage = Homepage(self.driver)
        homepage.getName().send_keys("Kavya")
        homepage.getEmail().send_keys("kavyap289@gmail.com")
        homepage.getPassword().send_keys("12345")
        gender = Select(homepage.getGender())
        gender.select_by_visible_text("Female")
        homepage.Submit().click()
        msg = homepage.getSuccess().text
        print(msg)
        time.sleep(5)
        #shop
        homepage.shop.click()
        checkoutpage = CheckOutPage(self.driver)
        names = checkoutpage.getCheckOutItems()
        i= -1
        for name in names:
            i= i+1
            cardtext = name.text
            if cardtext =='Blackberry':
                checkoutpage.AddToCart()[i].click()
        checkoutpage.getCheckOutButton().click()
        checkoutpage.getFinalCheckOut().click()
        #confirmation
        confirmpage = ConfirmPage(self.driver)
        confirmpage.getCountry().send_keys("Ind")
        self.verifyPresenceOfElement("India")
        confirmpage.getCountryvalue().click()
        confirmpage.getCheckBox().click()
        confirmpage.getPurchaseButton().click()



