from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
use_step_matcher("re")
driver=webdriver.Chrome()



@before_scenario(context,scenario)
def beforemethod():
    driver.get(url)

@after_scenario(context,scenario)

@given("Open browser")
def step_impl(context):
    print("Browser name=" +driver.name)


@When('Enter email "(?P<email>.+)" and password "(?P<password>.+)"')
def step_impl(context, email, password):
    driver.find_element(By.XPATH,"//input[@type='email']").send_keys("kavyap2899@gmail.com")
    driver.find_element(By.XPATH,"//input[@type='password']").send_keys("987654")




@then("Click signup button for successfull registarion")
def step_impl(context):
    driver.find_element(By.XPATH,"//button[@class='xcl-button-gr button-signin test_loginButton']").click()

time.sleep(5)


@step('Enter email "(?P<email>.+)" and password "(?P<password>.+)"')
def step_impl(context, email, password):
    """
    :type context: behave.runner.Context
    :type email: str
    :type password: str
    """
    raise NotImplementedError(u'STEP: And Enter email "<email>" and password "<password>"')