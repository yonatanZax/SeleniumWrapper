
class Find:

    def __init__(self, driver):
        self.driver = driver

    # driver.find_element_by_id("something")
    def findElementByID(self, idAsString):
        element = self.driver.find_element_by_id(idAsString)
        return element

    # driver.find_element_by_name('something')
    def findElementByName(self, nameAsString):
        element = self.driver.find_element_by_name(nameAsString)
        return element

    # driver.find_element_by_xpath("//*[@class = "something"]')
    def findElementByClass(self,classNameAsString):
        xpath = '//*[@class="%s" ]' % (classNameAsString,)
        element = self.driver.find_element_by_xpath(xpath);
        return element

    # driver.find_element_by_xpath('//*[@title="somthing"]')
    def findElementByTitle(self, titleAsString):
        xpath = '//*[@title="%s"]' % (titleAsString,)
        element = self.driver.find_element_by_xpath(xpath)
        return element

    # driver.find_element_by_xpath('//*[@aria-label="somthing"]')
    def findElementByAriaLabel(self, aria_labelAsString):
        xpath = '//*[@aria-label="%s"]' % (aria_labelAsString,)
        element = self.driver.find_element_by_xpath(xpath)
        return element

    # driver.find_element_by_link_text("CSV")
    def findElementByLinkText(self, linkTextAsString):
        element = self.driver.find_element_by_link_text(linkTextAsString)
        return element

    # driver.find_element_by_xpath('//a[@href="'+url+'"]')
    def findElementByHref(self,hrefAsString):
        href = '//a[@href="%s"]' % (hrefAsString,)
        element = self.driver.find_element_by_xpath(href)
        return element

    # url = browser.find_element_by_xpath("//a").get_attribute("data-href")
    def getElement_href(self,element):
        element.get_attribute("href")



