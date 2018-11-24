from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains





class Keyboard:

    def __init__(self,Driver):
        self.driver = Driver.driver
        self.actions = ActionChains(self.driver)
        self.Keys = Keys

    def writeTextToElement(self, element, inputAsString):
        element.send_keys(inputAsString)

    def pressAnyKey(self,Key):
        self.actions.send_keys(Key).perform()






class Mouse:

    def __init__(self,Driver):
        self.driver = Driver.driver

    def clickOnAnElement(self, element):
        element.click()














