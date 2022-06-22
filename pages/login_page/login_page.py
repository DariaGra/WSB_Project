from pages.base_page import BasePage
from config import LOGIN_URL
from pages.login_page.selectors import LOGIN_LOCATORS


class LoginPage(BasePage):
    _locators = LOGIN_LOCATORS
    _url = LOGIN_URL
    _form = LOGIN_LOCATORS['login_form']

    def __init__(self, driver):
        super().__init__(driver)
        self.go_to(self._url)

    def login_with(self, email="", password=""):
        self.fill(self._form['email'], email)
        self.fill(self._form['password'], password)
        self.click_submit_btn()

    def click_submit_btn(self):
        self.click_btn(self._form['submit_btn'])

    def get_error_message(self, field):
        return self.get_message(self._form[field]['error_msg'])

    def get_error_messages_count(self):
        errors = self.find_elements(self._locators['validation_error_msgs'])
        return len(errors)

    def get_login_success_message(self):
        return self.get_message(self._locators['login_success_msg'])
