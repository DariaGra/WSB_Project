import pytest
from .base_test import TestBase
from pages.registration_page.messages import REGISTRATION_MESSAGES
from pages.registration_page.registration_page import RegistrationPage


@pytest.mark.usefixtures('set_email_and_tag_attribute')
class TestRegistrationPage(TestBase):
    _error_msgs = REGISTRATION_MESSAGES['error_msgs']
    _success_msgs = REGISTRATION_MESSAGES['success_msgs']

    @pytest.fixture(autouse=True)
    def setup(self):
        self.register = RegistrationPage(self.driver)
        yield
        self.driver.delete_all_cookies()

    def test_register_with_empty_form(self):
        self.register.register_with()
        assert self._error_msgs['email'] == self.register.get_error_message_for_filed('email')
        assert self._error_msgs['password'] == self.register.get_error_message_for_filed('password')
        assert self._error_msgs['terms_and_conditions'] == self.register.get_error_message_for_filed('terms_and_conditions')
        assert self.register.get_error_messages_count() == 3

    def test_register_with_invalid_email(self):
        self.register.register_with(
            email='invalid_email',
            password='123qwe',
            rpassword='123qwe',
            newsletter=True,
            terms_and_conditions=True
        )
        assert self._error_msgs['email'] == self.register.get_error_message_for_filed('email')
        assert self.register.get_error_messages_count() == 1

    def test_register_with_terms_and_conditions_not_selected(self):
        self.register.register_with(
            email='iko.asdas@vp.ppl',
            password='123qwe',
            rpassword='123qwe',
            newsletter=True,
            terms_and_conditions=False
        )
        assert self._error_msgs['terms_and_conditions'] == self.register.get_error_message_for_filed('terms_and_conditions')
        assert self.register.get_error_messages_count() == 1

    def test_register_without_password(self):
        self.register.register_with(
            email='validmail@gggg.pl',
            password='',
            rpassword='1223qwe',
            newsletter=True,
            terms_and_conditions=True
        )
        assert self._error_msgs['password'] == self.register.get_error_message_for_filed('password')
        assert self._error_msgs['rpassword'] == self.register.get_error_message_for_filed('rpassword')
        assert self.register.get_error_messages_count() == 2

    def test_register_with_password_less_then_minimum_length(self):
        self.register.register_with(
            email='validmail@gggg.pl',
            password='dom',
            rpassword='dom',
            newsletter=True,
            terms_and_conditions=True
        )
        assert self._error_msgs['password'] == self.register.get_error_message_for_filed('password')
        assert self.register.get_error_messages_count() == 1

    def test_register_with_different_confirmation_password(self):
        self.register.register_with(
            email='validmail@gggg.pl',
            password='123qwe',
            rpassword='qweqwe',
            newsletter=True,
            terms_and_conditions=True
        )
        assert self.register.get_error_messages_count() == 1
        assert self._error_msgs['rpassword'] == self.register.get_error_message_for_filed('rpassword')

    def test_register_with_valid_data(self):
        self.register.register_with(
            email=self.email,
            password='123qwe',
            rpassword='123qwe',
            newsletter=True,
            terms_and_conditions=True
        )
        self.register.confirm_email(self.email, self.tag)
        assert self._success_msgs['registration_success_msg'] == self.register.get_success_registration_message()

    def test_register_with_email_already_registered(self):
        self.register.register_with(
            email=self.email,
            password='123qwe',
            rpassword='123qwe',
            newsletter=True,
            terms_and_conditions=True
        )
        assert self._error_msgs['registration_fail_msg'] == self.register.get_fail_registration_message()
