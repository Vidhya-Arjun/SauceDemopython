import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from POM.SauceDemoLogin import SauceDemoLogin

def reusable_method(browser_start, username, password):
    driver = browser_start
    sauce = SauceDemoLogin(driver)
    sauce.setUserName(username)
    sauce.setPassword(password)
    sauce.loginclick()
    return sauce

def test_valid_url(browser_start):
    driver = browser_start
    sauce = SauceDemoLogin(driver)

    title = sauce.gettitle()

    assert title == "Swag Labs" ,"Incorrect title"

def test_user_validation_test_login(browser_start):
    driver = browser_start
    sauce = reusable_method(driver, "standard_user", "secret_sauce")

    Dashboard_url = sauce.currentUrl()


    assert Dashboard_url =="https://www.saucedemo.com/inventory.html", "Incorrect url"


def test_invalid_user_validation_login(browser_start):
    driver = browser_start

    sauce = reusable_method(driver,"locked_out_user", "secret_sauce")
    error_msg = sauce.invalid_message()


    assert error_msg == "Epic sadface: Sorry, this user has been locked out.", "Incorrect error"

def test_problematic_user_validation_login(browser_start):
    driver = browser_start

    sauce = reusable_method(driver,"problem_user", "secret_sauce")

    Dashboard_url = sauce.currentUrl()


    assert  Dashboard_url =="https://www.saucedemo.com/inventory.html", "Incorrect url"


def test_performance_user_validation_login(browser_start):
    driver = browser_start

    sauce = reusable_method(driver,"performance_glitch_user", "secret_sauce")

    Dashboard_url = sauce.currentUrl()


    assert Dashboard_url == "https://www.saucedemo.com/inventory.html", "Incorrect url"

def test_error_user_validation_login(browser_start):
    driver = browser_start

    sauce = reusable_method(driver,"error_user", "secret_sauce")

    Dashboard_url = sauce.currentUrl()


    assert Dashboard_url == "https://www.saucedemo.com/inventory.html", "Incorrect url"


def test_visual_user_validation_login(browser_start):
    driver = browser_start


    sauce = reusable_method(driver,"visual_user", "secret_sauce")

    Dashboard_url = sauce.currentUrl()

    assert Dashboard_url == "https://www.saucedemo.com/inventory.html", "Incorrect url"


def test_log_out_user_validation_login(browser_start):
    driver = browser_start

    test_valid_url(driver)
    test_user_validation_test_login(driver)

    sauce = SauceDemoLogin(driver)
    sauce.logout()


    driver.back()

    assert driver.current_url == "https://www.saucedemo.com/", "User not logged out properly, verify the logout steps"
    assert driver.get_cookie("session-username") is None, "Incorrect navigation"



