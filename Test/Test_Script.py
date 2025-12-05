import pytest
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


from POM.SauceDemoLogin import SauceDemoLogin

def test_valid_url(browser_start):
    driver = browser_start
    sauce = SauceDemoLogin(driver)
    print(sauce.gettitle())
    title = sauce.gettitle()
    assert title == "Swag Labs" ,"Incorrect title"

def test_user_validation_test_login(browser_start):
    driver = browser_start
    sauce = SauceDemoLogin(driver)
    sauce.getUserName("standard_user")
    sauce.getPassword("secret_sauce")
    sauce.loginclick()
    Dashboard_url = sauce.currentUrl()
    driver.quit()
    assert Dashboard_url =="https://www.saucedemo.com/inventory.html", "Incorrect url"


def test_invalid_user_validation_login(browser_start):
    driver = browser_start
    sauce = SauceDemoLogin(driver)
    sauce.getUserName("locked_out_user")
    sauce.getPassword("secret_sauce")
    sauce.loginclick()
    error_msg = sauce.invalid_message()
    print('error_msg',error_msg)
    assert error_msg == "Epic sadface: Sorry, this user has been locked out.", "Incorrect error"

def test_problematic_user_validation_login(browser_start):
    driver = browser_start
    sauce = SauceDemoLogin(driver)
    sauce.getUserName("problem_user")
    sauce.getPassword("secret_sauce")
    sauce.loginclick()

    Dashboard_url = sauce.currentUrl()
    driver.quit()

    assert  Dashboard_url =="https://www.saucedemo.com/inventory.html", "Incorrect url"


def test_performance_user_validation_login(browser_start):
    driver = browser_start
    sauce = SauceDemoLogin(driver)
    sauce.getUserName("problem_user")
    sauce.getPassword("secret_sauce")
    sauce.loginclick()

    Dashboard_url = sauce.currentUrl()
    driver.quit()

    assert Dashboard_url == "https://www.saucedemo.com/inventory.html", "Incorrect url"

def test_error_user_validation_login(browser_start):
    driver = browser_start
    sauce = SauceDemoLogin(driver)
    sauce.getUserName("error_user")
    sauce.getPassword("secret_sauce")
    sauce.loginclick()

    Dashboard_url = sauce.currentUrl()
    driver.quit()

    assert Dashboard_url == "https://www.saucedemo.com/inventory.html", "Incorrect url"


def test_visual_user_validation_login(browser_start):
    driver = browser_start
    sauce = SauceDemoLogin(driver)
    sauce.getUserName("visual_user")
    sauce.getPassword("secret_sauce")
    sauce.loginclick()

    Dashboard_url = sauce.currentUrl()
    driver.quit()
    assert Dashboard_url == "https://www.saucedemo.com/inventory.html", "Incorrect url"






