import FindElement
import DriverClass
import Inputs
import time

symbol = "EBAY"

page_load_timeOut = 30


Driver = DriverClass.Driver('Chrome', loadTimeInSeconds=page_load_timeOut)
URL = "https://finance.yahoo.com/"
Driver.openWebsite(url=URL)

# driver = Driver.getDriver()

elm_searchBar = Driver.Find.findElementByName("yfin-usr-qry")
keyboard = Inputs.Keyboard(Driver)
mouse = Inputs.Mouse(Driver)
keyboard.writeTextToElement(element=elm_searchBar, inputAsString=symbol)

time.sleep(3)
elm_searchBtn = Driver.Find.findElementByID("search-button")
mouse.clickOnAnElement(element=elm_searchBtn)


time.sleep(10)
Driver.close()
# driver.quit()















