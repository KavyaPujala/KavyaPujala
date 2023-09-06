import pytest
from selenium import webdriver

from selenium.webdriver.common.by import By


@pytest.fixture()
def setup(request):
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    request.cls.driver=driver
    yield
    driver.close()

