import pytest
from .base_test import TestBase
from pages.login_page.messages import LOGIN_MESSAGES
from pages.login_page.login_page import LoginPage


class TestLoginPage(TestBase):
    _error_msgs = LOGIN_MESSAGES['error_msgs']
    _success_msgs = LOGIN_MESSAGES['success_msgs']

    @pytest.fixture(autouse=True)
    def setup(self):
        self.login = LoginPage(self.driver)
        yield
        self.driver.delete_all_cookies()

    def test_login_with_empty_form(self):
        self.login.login_with()
        assert self._error_msgs['email'] == self.login.get_error_message('email')
        assert self._error_msgs['password'] == self.login.get_error_message('password')
        assert self.login.get_error_messages_count() == 2

    def test_login_with_invalid_email(self):
        self.login.login_with(
            email='invalid email',
            password='qwe123'
        )
        assert self._error_msgs['email'] == self.login.get_error_message('email')
        assert self.login.get_error_messages_count() == 1

    def test_login_with_invalid_password(self):
        self.login.login_with(
            email='valid@vp.pl',
            password='q13',
        )
        assert self._error_msgs['password'] == self.login.get_error_message('password')
        assert self.login.get_error_messages_count() == 1

    def test_login_with_valid_data(self):
        self.login.login_with(
            email=self.login_email,
            password=self.login_password,
        )
        assert self._success_msgs['success_msg'] == self.login.get_login_success_message()