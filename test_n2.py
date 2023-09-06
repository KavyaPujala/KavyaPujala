import pytest
import time
from pynput.keyboard import Key, Controller
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from KavyaPython.Xpath import driver
from KavyaPython.pageobjects.njob import Njob
from KavyaPython.pageobjects.nlogin import nlogin
from KavyaPython.pageobjects.nhome import nhome
@pytest.mark.usefixtures("setup")
class TestTwo:

    def test_n2(self):
        Nlogin = nlogin(self.driver)
        time.sleep(2)
        Nlogin.getUserName().send_keys("Admin")
        time.sleep(2)
        Nlogin.getPassword().send_keys("admin123")
        time.sleep(2)
        Nlogin.getLogin().click()
        time.sleep(2)
        #PIM
        NHome = nhome(self.driver)
        time.sleep(2)
        NHome.getPim().click()
        time.sleep(2)
        NHome.getAddemployee().click()
        time.sleep(2)
        NHome.getFirstname().send_keys("Surya")
        #time.sleep(2)
        NHome.getLastname().send_keys("S")
        #time.sleep(2)
        NHome.getEmployeeid().send_keys("345")
        #time.sleep(2)
        NHome.getProfile().click()
        time.sleep(2)
        actions = ActionChains(self.driver)
        actions.send_keys("pictures")
        actions.send_keys(Keys.ARROW_DOWN)
        actions.send_keys(Keys.ENTER)
        time.sleep(2)
        actions.send_keys("Screensh")
        actions.send_keys(Keys.ARROW_DOWN)
        actions.send_keys(Keys.ENTER)
        actions.send_keys("scr")
        actions.send_keys(Keys.ARROW_DOWN)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        NHome.getSwitch().click()
        time.sleep(2)
        NHome.getUsername().send_keys("Surya")
        time.sleep(2)
        NHome.getEnable().click()
        time.sleep(2)
        NHome.getPassword().send_keys("Surya345")
        time.sleep(2)
        NHome.getConfirmpassword().send_keys("Surya345")
        time.sleep(2)
        NHome.getSave().click()
        time.sleep(20)

        #Job Details
        NJob = Njob(self.driver)
        NJob.getJob().click()
        time.sleep(2)

        #Job Category
        NJob.getJobcategory().click()
        time.sleep(4)
        actions = ActionChains(self.driver)
        actions.send_keys("c")
        actions.send_keys("Key.ARROW_DOWN")
        actions.send_keys("Key.ENTER")
        actions.perform()
        time.sleep(2)

        #Job Title
        NJob.getJobtitle().click()
        time.sleep(4)
        actions = ActionChains(self.driver)
        actions.send_keys("a")
        actions.send_keys("Key.ARROW_DOWN")
        actions.send_keys("Key.ENTER")
        actions.perform()
        time.sleep(2)

        NJob.getSave().click()
        time.sleep(4)

        '''actual = Njob.getNeelima().text
        expected_text = "Neelima"
        assert actual == expected_text
        time.sleep(2)
        print("Successfully compared")'''