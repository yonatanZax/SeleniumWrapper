
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import FindElement
import os
CHROME = 'Chrome'
FIRE_FOX = 'Firefox'
EXPLORER = 'Explorer'


RelativeDriversFolder = 'Drivers/'
# D:\PythonProjectInD\SeleniumDLL\Drivers
driversPath = os.path.abspath(os.path.join(os.path.dirname(__file__), RelativeDriversFolder))
RelativeDownloadFolder = 'SeleniumDownloads/'
# D:\PythonProjectInD\SeleniumDLL\SeleniumDownloads
downloadPath = os.path.abspath(os.path.join(os.path.dirname(__file__), RelativeDownloadFolder))


def initDirectories():
    import os

    if not os.path.exists(driversPath):
        print("\n** Drivers folder doesn't exists :(")

    if not os.path.exists(downloadPath):
        os.mkdir(downloadPath)



class Driver:

    def __init__(self, driverTypeAsString, loadTimeInSeconds=30):
        RelativeDriversFolder = 'Drivers/'
        # D:\PythonProjectInD\SeleniumDLL\Drivers
        self.driversPath = driversPath
        RelativeDownloadFolder = 'SeleniumDownloads/'
        # D:\PythonProjectInD\SeleniumDLL\SeleniumDownloads
        self.downloadPath = downloadPath

        driver = None

        if driverTypeAsString == CHROME:
            # Set driver preferences
            chromeOptions = webdriver.ChromeOptions()
            prefs = {"download.default_directory": self.downloadPath}
            chromeOptions.add_experimental_option("prefs", prefs)

            driver = webdriver.Chrome(executable_path=self.driversPath + "/chromedriver.exe",chrome_options=chromeOptions)
        elif driverTypeAsString == FIRE_FOX:
            print('Enter firefox_binary')
            # cap = DesiredCapabilities().FIREFOX
            # cap["marionette"] = False
            # driver = webdriver.Firefox(capabilities=cap,executable_path=self.driversPath + '/geckodriver.exe')
        elif driverTypeAsString == EXPLORER:
            driver = webdriver.Ie(executable_path=self.driversPath + "/explorerdriver.exe")


        self.driver = driver
        self.driver.set_page_load_timeout(loadTimeInSeconds)
        self.Find = FindElement.Find(self.driver)



    def getDriver(self):
        return self.driver

    def setLoadTimeout(self, loadTimeInSeconds):
        self.driver.set_page_load_timeout(loadTimeInSeconds)

    def openWebsite(self,url):
        self.driver.get(url)

    def close(self):
        self.driver.quit()
        print('*** Driver closed successfully ***')







