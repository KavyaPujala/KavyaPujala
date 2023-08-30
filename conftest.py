import pytest
from selenium
from selenium.webdriver.chrome import webdriver


#import time
@pytest.fixture()
def setup(request):
    driver = webdriver.Chrome()
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/cart")
    driver.maximize_window()
    request.cls.driver=driver
    yield
    print("Test ended")
    driver.close()
#time.sleep(10)