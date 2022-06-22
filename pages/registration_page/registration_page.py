from pages.base_page import BasePage
from config import REGISTRATION_URL, SENDER_EMAIL
from helpers import get_confirmation_link
from pages.registration_page.selectors import REGISTRATION_LOCATORS


class RegistrationPage(BasePage):
    _locators = REGISTRATION_LOCATORS
    _url = REGISTRATION_URL
    _form = REGISTRATION_LOCATORS['registration_form']
    _sender = SENDER_EMAIL

    def __init__(self, driver):
        super().__init__(driver)
        self.go_to(self._url)

    def register_with(self, email="", password="", rpassword="", newsletter=False, terms_and_conditions=False):
        self.fill(self._form['email'], email)
        self.fill(self._form['password'], password)
        self.fill(self._form['rpassword'], rpassword)
        self.click_checkbox(self._form['newsletter'], newsletter)
        self.click_checkbox(self._form['terms_and_conditions'], terms_and_conditions)
        self.click_submit_btn()

    def click_submit_btn(self):
        # Submit registration form
        self.click_btn(self._locators['submit_btn'])

    def get_error_message_for_filed(self, field):
        """
        Return error message related to form filed if present.
        :param field: (str) input field name
        :return:
            error_message (str)
        """
        return self.get_message(self._form[field]['error_msg'])

    def get_error_messages_count(self):
        # Return numbers of error messages
        errors = self.find_elements(self._locators['error_msgs'])
        return len(errors)

    def get_fail_registration_message(self):
        return self.get_message(self._locators['registration_fail_msg'])

    def get_success_registration_message(self):
        return self.get_message(self._locators['registration_success_msg'])

    def confirm_email(self, email, tag):
        confirmation_link = get_confirmation_link(
            sender=self._sender,
            receiver=email,
            tag=tag,
            subject="Rejestracja użytkownika"
        )
        self.go_to(confirmation_link)
