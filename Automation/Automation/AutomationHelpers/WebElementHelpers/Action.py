from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class Action(object):
    """Class responsible for performing the actions on the webelements"""
    #Private variable to initialize the driver
    __driver__=None

    def __init__(self,driver):
        self.__driver__ = driver;
        __defaultWaitTime__ = 60

    def __findElementClickableElement__(self,locator):
        WebDriverWait(self.__driver__,60).until(EC.element_to_be_clickable(locator))
        return self.__driver__.find_element(locator[0],locator[1])

    def __findElementVisibleElement__(self,locator):
        WebDriverWait(self.__driver__,60).until(EC.visibility_of_element_located(locator))
        return self.__driver__.find_element(locator[0],locator[1])

    def click(self,locator):
        #Wait for the element to be clickable
        element = self.__findElementClickableElement__(locator)
        element.click()
   
    def sendKeys(self,locator,value):
        #Wait for the elemetn to be clickable
        element = self.__findElementClickableElement__(locator)
        element.clear()
        element.send_keys(value)

    def selectByTextFromDropDown(self,locator,text):
        element = self.__findElementClickableElement__(locator)
        select = Select(element)
        select.select_by_visible_text(text)