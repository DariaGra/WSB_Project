import pytest
from tests.base_test import TestBase
from pages.payments_page.payments_page import PaymentsPage
from pages.item_page.item_page import ItemPage


class TestPaymentsPage(TestBase):

    @pytest.fixture(autouse=True)
    def setup(self):
        self.payments = PaymentsPage(self.driver)
        self.item = ItemPage(self.driver)
        yield
        self.driver.delete_all_cookies()

    def test_buy_without_login(self):
        self.item.add_item_to_cart()
        self.payments.buy_without_login()
        assert self.payments.successful_buy() == 'Twoje zamówienie zostało złożone!'

    def test_buy_with_login(self):
        self.item.add_item_to_cart()
        self.payments.buy_with_login(self.login_email, self.login_password)
        assert self.payments.successful_buy() == 'Twoje zamówienie zostało złożone!'

    def test_buy_without_login_firm(self):
        self.item.add_item_to_cart()
        self.payments.buy_without_login_firm()
        assert self.payments.successful_buy() == 'Twoje zamówienie zostało złożone!'

