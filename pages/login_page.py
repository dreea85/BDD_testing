from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    LOGIN_PAGE_URL = "https://magento.softwaretestingboard.com/customer/account/login"
    INPUT_EMAIL = (By.NAME, "login[username]")
    INPUT_PASSWORD = (By.NAME, "login[password]")
    BUTTON_LOGIN = (By.CSS_SELECTOR, "fieldset>div>div>button>span")
    ERROR_MSG_MAIN = (By.XPATH, '//div[contains(text(),"The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later.")]')



    def navigate_to_login_page(self):
        self.browser.get(self.LOGIN_PAGE_URL)

    def set_email(self, email):
        self.type(self.INPUT_EMAIL, email)

    def set_password(self):
        self.type(self.INPUT_PASSWORD, "123")

    def click_login_button(self):
        self.click(self.BUTTON_LOGIN)

    def get_main_error_message(self):
        return self.get_text(self.ERROR_MSG_MAIN)