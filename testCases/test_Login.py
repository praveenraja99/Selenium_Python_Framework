import time
from selenium import webdriver
import  pytest
from pageObjects.LoginPage import Login
from testCases.conftest import setup,pytest_addoption,browser
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_Login_SC001():
    # class virables
    base_url = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    #return logger object and store in a variable and by using that object access the logs
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle_TC001(self,setup):
        self.logger.info(" ***************************Verifying test_homePageTitle_TC001*************** ")
        #setUp method will be called and return driver instance
        self.driver = setup
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(self.base_url)
        act_title = self.driver.title

        if act_title == "XD Brain":
            assert True
            self.driver.close()
            self.logger.info(" *****************Home page title test is passed************************* ")
        else:
            self.driver.save_screenshot("../Screenshots/test_homePageTitle_TC001.png")
            self.driver.close()
            self.logger.info(" *****************Home page title test is failed************************* ")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Login_TC002(self,setup):
        self.logger.info(" ***************************Verifying test_Login_TC002*************** ")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(self.base_url)
        # create object for Login class to access page object methods
        Lp = Login(self.driver)  #it will call default constructor in Login class during object creation
        Lp.setUsername(self.username)
        Lp.setPassword(self.password)
        Lp.click_Login()
        time.sleep(2)
        login_title = self.driver.title
        print(login_title)
        self.driver.close()
        if login_title == "XD Brain":
            self.logger.info("*****************After Login page title test is passed*************************")
            assert True
        else:
            self.logger.info("*****************After Login page title test is failed*************************")
            assert False

    @pytest.mark.sanity
    def test_Logout_TC003(self,setup):
        self.logger.info("***************************Verifying test_Logout_TC003***************")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(self.base_url)
        # create object for Login class to access page object methods
        Lp = Login(self.driver)  # it will call default constructor in Login class during object creation
        Lp.setUsername(self.username)
        Lp.setPassword(self.password)
        Lp.click_Login()
        time.sleep(2)
        login_title = self.driver.title
        print(login_title)
        Lp.click_Logout()
        time.sleep(3)
        if login_title == "XD Brain":
            assert True
            self.driver.close()
            self.logger.info("*****************After Logout page title test is passed*************************")
        else:
            self.driver.save_screenshot("../Screenshots/test_Logout_TC003.png")
            self.driver.close()
            self.logger.info("*****************After Logout page title test is Failed*************************")
            assert False






