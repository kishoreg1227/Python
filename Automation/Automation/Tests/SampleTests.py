import unittest
import AutomationHelpers.DriverHelpers.DriverFactory as driverFactory
import Pages.BasePage as basePage

class SampleTests(unittest.TestCase):
    
    __driver__ = None
    __basePage__ = None
    __homePage__ = None
    __registrationPage__= None

    def setUp(self):
        dfactory = driverFactory.DriverFactory('chrome')
        self.__driver__ = dfactory.LaunchDriver()
        self.__basePage__ = basePage.BasePage(self.__driver__)
        self.__homePage__ = self.__basePage__.navigateToURL("http://newtours.demoaut.com/mercurywelcome.php")
    
    def test_navigateToRegistrationPage(self):
        self.__homePage__.navigateToRegistrationPage()

    def test_Registration(self):
        self.__registrationPage__ = self.__homePage__.navigateToRegistrationPage()
        self.__registrationPage__.enterContactInformation()
        self.__registrationPage__.enterMailingInformation()
        self.__registrationPage__.enterUserInformation()

    def tearDown(self):
        self.__driver__.quit()