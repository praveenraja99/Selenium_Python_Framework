import time
from selenium import webdriver
import  pytest
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import Login
from testCases.conftest import setup
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import ExcelUtils

class Test_DDT_Login_SC001():
    # class virables
    base_url = ReadConfig.getApplicationUrl()
    #Test data file path
    TestData_path = "../TestData/Login_Testdata.xlsx"
    SheetName = ReadConfig.getSheetName()
    #return logger object and store in a variable and by using that object access the logs
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_DDT_Logout_TC001(self,setup):
        self.logger.info("***************************Verifying test_Logout_TC003***************")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.implicitly_wait(6)
        self.driver.get(self.base_url)
        # create object for Login class to access page object methods
        self.Lp = Login(self.driver)  # it will call default constructor in Login class during object creation

        self.rows = ExcelUtils.getRowCount(self.TestData_path,self.SheetName)
        self.column = ExcelUtils.getColumnCount(self.TestData_path,self.SheetName)
        print("Number of rows in excel:", self.rows )
        print("Number of column in excel:", self.column)

        #declaring empty list variable inorder to capture list of test case status
        self.list_status = []

        # '2' is used in range to ignore 1st row as it has heading
        # rows+1 -->becaus in range last row will not taken so +1 is added.
        for r in range(2,self.rows):

           self.username = ExcelUtils.readData(self.TestData_path,self.SheetName,r,1)
           self.password = ExcelUtils.readData(self.TestData_path, self.SheetName, r, 2)
           self.expected_result = ExcelUtils.readData(self.TestData_path, self.SheetName, r, 3)
           print("expected Result:", self.expected_result)

           self.Lp.setUsername(self.username)
           print("username is :", self.username)
           self.Lp.setPassword(self.password)
           self.Lp.click_Login()
           time.sleep(2)

           self.act_Logo = self.Lp.HomePageLogo()
           self.exp_Logo = "COMPANY_LOGO"
           print("Logo name :", self.act_Logo)

           if self.act_Logo == self.exp_Logo: #checking whether successfully logged/not
               if self.expected_result == "Pass":  # if matches my expected result then test case is passed
                   self.logger.info("######PASSED ####################")
                   self.Lp.click_Logout()
                   time.sleep(2)
                   self.list_status.append("Pass")

               elif self.expected_result == "Fail": # if not matching with expected result then test case is failed
                   self.logger.info("######FAILED ####################")
                   #self.Lp.click_Logout()
                   self.list_status.append("Fail")

           elif self.act_Logo != self.exp_Logo:  #checking whether successfully logged/not
               if self.expected_result == "Pass":  # if matches my expected result then test case is passed
                   self.logger.info("######FAILED ####################")

                   self.list_status.append("Fail")

               elif self.expected_result == "Fail": # if not matching with expected result then test case is failed
                   self.logger.info("######PASSED ####################")

                   self.list_status.append("Pass")

           #checking in my list whether fail status is not present
        if "Fail"  not in self.list_status:
                self.logger.info("######LOGIN DDT PASSED ####################")
                self.driver.close()
                assert True
        else:
                self.logger.info("######LOGIN DDT FAILED ####################")
                self.driver.close()
                assert False

        self.logger.info("######END OF test_DDT_Logout_TC001 testing ####################")






