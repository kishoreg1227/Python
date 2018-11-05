from AutomationHelpers.WebElementHelpers.Action import Action
from Pages.HomePage import *

class BasePage(object):
    #Base Page for creating all the pages objects
    Action = None

    def __init__(self,driver):
        self.Driver = driver
        self.Action = Action(driver)

    def navigateToURL(self,url):
        self.Driver.get(url)
        return HomePage(self.Action)