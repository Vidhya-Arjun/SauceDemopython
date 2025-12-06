import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chromium import options


@pytest.fixture(scope="function")
def browser_start():

    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)

    driver.get("https://www.saucedemo.com/")
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
