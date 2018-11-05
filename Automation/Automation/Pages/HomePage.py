from selenium.webdriver.common.by import By
from Pages.RegistrationPage import RegistrationPage

class HomePage(object):
    
    __registerPageLinkLocator__ = (By.XPATH,"//*[contains(text(),'REGISTER')]")
    __actionObject__ = None

    def __init__(self,action):
        self.__actionObject__ = action

    def navigateToRegistrationPage(self):
        self.__actionObject__.click(self.__registerPageLinkLocator__)
        return RegistrationPage(self.__actionObject__)