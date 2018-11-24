import FindElement
import DriverClass
import Inputs
import time

page_load_timeOut = 30

Driver = DriverClass.Driver('Chrome', loadTimeInSeconds=page_load_timeOut)
URL = "https://www.youtube.com/"
Driver.openWebsite(url=URL)

keyboard = Inputs.Keyboard(Driver)
mouse = Inputs.Mouse(Driver)

elm_searchBar = Driver.Find.findElementByID(idAsString='search')
line_to_search = "Jonas Blue - Rise ft. Jack & Jack"
keyboard.writeTextToElement(element=elm_searchBar,inputAsString=line_to_search)
keyboard.pressAnyKey(keyboard.Keys.ENTER)

time.sleep(2)
elm_videoTitle = Driver.Find.findElementByTitle(titleAsString=line_to_search)
mouse.clickOnAnElement(elm_videoTitle)

time.sleep(45)

# *Pause* video
# Space in the keyboard pauses the video
keyboard.pressAnyKey(keyboard.Keys.SPACE)



time.sleep(5)
# Close all...
Driver.close()









