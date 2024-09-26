import configparser


# Initialize configparser (create object)
config = configparser.RawConfigParser()
# Read the config file
config.read("../Configurations/config.ini")

class ReadConfig: #parenthesis is not mandatory for class

#keeping all the methods as static inorder to access the method without creating an object
# self is not required as it is static method
    @staticmethod
    def getApplicationUrl():
      url =  config.get('XDB_URL','base_url')
      return url

    @staticmethod
    def getUsername():
        username = config.get('XDB_Login_credentials','username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('XDB_Login_credentials','password')
        return password


    @staticmethod
    def getSheetName():
        SheetName = config.get('LoginTestdata', 'SheetName')
        return SheetName


