import time
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class Login():
    # capture all the required locators in login page
    username_xpath = "//input[@id='username']"
    password_xpath = "//input[@id='password']"
    login_button_xpath = "//input[@id='login']"
    # rememberMe_ckbox_xpath = "//input[@id='RememberMe']"
    setting_menu_xpath = "//div[@class='dropdown']//img[@alt='COMPANY_LOGO']"
    logout_option_xpath = "//a[normalize-space()='Logout']"
    homepageLogo_xpath = "//a[normalize-space()='']//img[@alt='COMPANY_LOGO']"


    # default constructor (passing driver to this class)
    def __init__(self,driver):
        self.driver = driver

    # Find elements and perform action

    def setUsername(self,username):
        usr_name = self.driver.find_element(By.XPATH,self.username_xpath)
        usr_name.clear()
        # time.sleep(2)
        usr_name.send_keys(username)

    def setPassword(self,password):
        pswd = self.driver.find_element(By.XPATH,self.password_xpath)
        pswd.clear()
        pswd.send_keys(password)

    def click_Login(self):
        Lgin_btn = self.driver.find_element(By.XPATH,self.login_button_xpath)
        Lgin_btn.click()

    # def click_rememberMe_ckBox(self):
    #     remember_ck_box = self.driver.find_element(By.XPATH,self.rememberMe_ckbox_xpath)
    #     remember_ck_box.click()

    def click_Logout(self):
        settings_menu = self.driver.find_element(By.XPATH,self.setting_menu_xpath)
        logout_option = self.driver.find_element(By.XPATH,self.logout_option_xpath)
        # To do mouse action we have to create an object using ActionChain class and pass the driver instance
        act = ActionChains(self.driver)
        act.move_to_element(settings_menu).move_to_element(logout_option).click().perform()
        # perform method must be used to perform the action

    def HomePageLogo(self):
        try:
            self.homePage_Logo = self.driver.find_element(By.XPATH, self.homepageLogo_xpath).get_attribute('alt')
            return self.homePage_Logo
        except NoSuchElementException:
            # Return None if the element is not found
            return None



