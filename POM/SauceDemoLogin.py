from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class SauceDemoLogin:

    usernameinput = "user-name"
    passwordinput = "password"
    loginbutton = "//input[@id = 'login-button']"
    error_message ="//h3[@data-test='error']"
    hamburger_menu_button = "//button[@id='react-burger-menu-btn']"
    logoutbutton = "//nav[@class='bm-item-list']/a[@id='logout_sidebar_link']"




    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    def gettitle(self):
        return self.driver.title
    def currentUrl(self):
        return self.driver.current_url

    # Consider renaming this method as it says "getUserName" but this method sends text to webelement
    def setUserName(self,username):
        self.driver.find_element(By.ID, self.usernameinput).send_keys(username)
    def setPassword(self,password):
        self.driver.find_element(By.ID, self.passwordinput).send_keys(password)
    def loginclick(self):
        self.driver.find_element(By.XPATH, self.loginbutton).click()

    def invalid_message(self):
        error_msg_element = self.wait.until(EC.presence_of_element_located((By.XPATH,self.error_message)))
        xpathfortext = error_msg_element.text
        return xpathfortext

    def waittime(self,wait_time):
        return WebDriverWait(self.driver, wait_time)

    # Separate the logic of this method
    # 1. open the hamburger menu,
    # 2. Click the Logout button
    def openhamburger(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH,self.hamburger_menu_button))).click()

    def logout(self):
        self.openhamburger()

        self.wait.until(EC.element_to_be_clickable((By.XPATH,self.logoutbutton))).click()




