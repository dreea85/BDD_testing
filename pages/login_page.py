from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    LOGIN_PAGE_URL = "https://www.betterworldbooks.com/account/login"
    INPUT_EMAIL = (By.ID, "loginEmail")
    INPUT_PASSWORD = (By.ID, "loginPassword")
    BUTTON_LOGIN = (By.CLASS_NAME, "form-control btn btn-success")
    ERROR_MSG_MAIN = (By.XPATH, '(//span[@class="validation-error"])[1]')



    def navigate_to_login_page(self):
        self.browser.get(self.LOGIN_PAGE_URL)

    def set_email(self):
        self.type(self.INPUT_EMAIL, "hihaho@yahoo.com")

    def set_password(self):
        self.type(self.INPUT_PASSWORD, "123")

    def click_login_button(self):
        self.click(self.BUTTON_LOGIN)

    def is_main_error_message_displayed(self):
        return self.find(self.ERROR_MSG_MAIN).is_displayed()