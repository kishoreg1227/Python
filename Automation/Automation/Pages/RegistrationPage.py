from selenium.webdriver.common.by import By
from AutomationHelpers.StringHelpers.StringHelpers import StringHelpers


class RegistrationPage(object):
    """Class representation of the registration page and it's page objects and actions"""
    __actionObject__ = None
    
    #Contact Information
    __fname__ = (By.NAME,"firstName")
    __lname__ = (By.NAME,"lastName")
    __phoneNumber__ = (By.NAME,"phone")
    __email__ = (By.ID,"userName")
    
    #Mailing Information
    __address1__ = (By.NAME,"address1")
    __address2__ = (By.NAME,"address2")
    __city__ = (By.NAME,"city")
    __state__ = (By.NAME,"state")
    __postalcode__ = (By.NAME,"postalCode")
    __country__ = (By.NAME,"country")

    #User Information
    __userName__ = (By.ID,"email")
    __passwordLocator__ = (By.NAME,"password")
    __confirmPassword__ = (By.NAME,"confirmPassword")
    __submitButton__ = (By.NAME,"register")

    def __init__(self,action):
        self.__actionObject__ = action

    def enterContactInformation(self):
        self.__actionObject__.sendKeys(self.__fname__,"Kishore")
        self.__actionObject__.sendKeys(self.__lname__,"Kumar")
        self.__actionObject__.sendKeys(self.__phoneNumber__,"9502669933")
        self.__actionObject__.sendKeys(self.__email__,"kishoreg1227@gmail.com")

    def enterMailingInformation(self):
        self.__actionObject__.sendKeys(self.__address1__,"E02")
        self.__actionObject__.sendKeys(self.__address2__,"Lok Sangam Vihar")
        self.__actionObject__.sendKeys(self.__city__,"Pune")
        self.__actionObject__.sendKeys(self.__state__,"Maharastra")
        self.__actionObject__.sendKeys(self.__postalcode__,"411007")
        self.__actionObject__.selectByTextFromDropDown(self.__country__,"INDIA")

    def enterUserInformation(self):
        userNameGen = StringHelpers.UserIdGenerator()
        self.__actionObject__.sendKeys(self.__userName__,"Kishoreg"+ userNameGen)
        self.__actionObject__.sendKeys(self.__passwordLocator__,"Test123")
        self.__actionObject__.sendKeys(self.__confirmPassword__,"Test123")
        self.__actionObject__.click(self.__submitButton__);


