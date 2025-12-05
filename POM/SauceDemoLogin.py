from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class SauceDemoLogin:

    Usernameinput = "user-name"
    passwordinput = "password"
    loginbutton = "//input[@id = 'login-button']"
    error_message ="//h3[@data-test='error']"
    hamburger_menu_button = "//div[@class='bm-burger-button']/button[@id='react-burger-menu-btn']"
    loginbutton = "//nav[@class='bm-item-list']/a[@id='logout_sidebar_link']"


    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def gettitle(self):
        return self.driver.title
    def currentUrl(self):
        return self.driver.current_url
    def getUserName(self,username):
        return self.driver.find_element(By.ID, self.Usernameinput).send_keys(username)
    def getPassword(self,password):
        return self.driver.find_element(By.ID, self.passwordinput).send_keys(password)
    def loginclick(self):
        return self.driver.find_element(By.XPATH, self.loginbutton).click()

    def invalid_message(self):
        wait_time = self.wait.until(EC.presence_of_element_located((By.XPATH,self.error_message)))
        xpathfortext = wait_time.text
        return xpathfortext

    def waittime(self,wait_time):
        return WebDriverWait(self.driver, wait_time)

    def logout(self):
        self.driver.find_element(By.XPATH, self.hamburger_menu_button).click()
        return self.driver.find_element(By.XPATH, self.logout_button).click()

