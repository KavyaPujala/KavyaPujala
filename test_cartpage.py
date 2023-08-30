import pytest

import time

from pageobjects.carthomepage import Carthomepage

time.sleep(5)


@pytest.mark.usefixtures("setup")
class TestOne:
    def testcartpage(self):
        carthomepage = Carthomepage(self.driver)
        products = carthomepage.getProducts()
        i=-1
        for product in products:
            i=i+1
            name=product.text
            if "Beetroot" in name:
                carthomepage.getAddtoCart()[i].click()
            elif "Carrot" in name:
                carthomepage.getAddtoCart()[i].click()
        carthomepage.getAddBucket().click()
        carthomepage.getCheckout().click()
