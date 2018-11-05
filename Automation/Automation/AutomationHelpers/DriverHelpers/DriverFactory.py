from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from AutomationHelpers.JSonHelpers.JSonConverter import JSonConverter as js

class DriverFactory(object):
    """Class responsible to create instance of the required driver type"""
    driverName = ''
    __driver__ = None

    def __init__(self,browser):
        self.driverName = browser

    def LaunchDriver(self):
        if self.driverName.lower() == 'chrome':
            self.__driver__  = webdriver.Chrome()
        elif self.driverName.lower() == 'firefox':
            self.__driver__ = webdriver.Firefox()
        elif self.driverName.lower() == 'edge':
            self.__driver__ = webdriver.Edge()
        elif self.driverName.lower() == 'remote':
            self.__driver__ = self.__launchRemoteDriver__()
        else:
            raise ValueError('The specified driver {} is invalid'.format(driverName))
        self.__driver__.maximize_window()
        return self.__driver__

    def __launchRemoteDriver__(self):
        jcobj = js.JSonConverter()
        data = jcobj.DeserializeJSonToObjects('ConfigurationFiles\BrowserConfigurations.json')
        if "cloud" in data["remoteExecution"]["type"]:
            desired_capabilities = data["cloudcaps"]
            return webdriver.Remote(data["remoteURL"]["url"],desired_capabilities)
        elif "grid" in data["remoteExecution"]["type"]:
            desired_capabilities = data["gridcaps"]
            return webdriver.Remote(data["remoteURL"]["url"],desired_capabilities)
        else:
            raise ValueError('Invalid configuration type {}'.format(data["remoteExecution"]["type"]))