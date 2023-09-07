from browser import Browser

class BasePage(Browser):
    BASE_URL = "https://www.betterworldbooks.com/"

    def find(self, locator):
        return self.browser.find_element(*locator)

    def type(self, locator, text):
        self.find(locator).send.keys(text)

    def click(self, locator):
        self.find(locator).click()