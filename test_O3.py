import logging
import time
import pytest
from selenium.webdriver import ActionChains, Keys

from pageobjects.OrangeHomePage import OrangeHomePage
from pageobjects.OrangeLoginPage import OrangeLoginPage

@pytest.mark.usefixtures("setup")
class TestTwo:

    def test_O3(self):
        log = self.getLogger()
        log.info("Execution started")
        Orangeloginpage = OrangeLoginPage(self.driver)
        Orangeloginpage.getUserName().send_keys("Admin")
        #time.sleep(2)
        Orangeloginpage.getPassword().send_keys("admin123")
        #time.sleep(2)
        Orangeloginpage.getLogin().click()
        #time.sleep(2)

        #Recruitment
        log.info("Entered recruitment page")
        orangehomePage = OrangeHomePage(self.driver)
        orangehomePage.getRecruitment().click()
        #time.sleep(2)
        orangehomePage.getCanditates().click()
        #time.sleep(2)
        orangehomePage.getType().click()
        time.sleep(2)
        actions = ActionChains(self.driver)
        actions.send_keys("mohan")
        actions.send_keys(Keys.ARROW_DOWN)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        time.sleep(2)

        orangehomePage.getSearch().click()
        time.sleep(4)
        actual = orangehomePage.getCompare().text
        expected_text = "mohan k"
        assert actual == expected_text
        time.sleep(2)
        print("Successfully compared")
        orangehomePage.getReset().click()
        time.sleep(4)


    def getLogger(self):
        logger = logging.getLogger(__name__)
        filehandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s :%(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.DEBUG)
        return logger