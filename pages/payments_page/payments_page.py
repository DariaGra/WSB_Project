from pages.base_page import BasePage
from config import CART_PAGE_URL
from pages.payments_page.selectors import PAYMENTS_LOCATORS
from selenium.webdriver.common.by import By

class PaymentsPage(BasePage):
    _locators = PAYMENTS_LOCATORS
    _url = CART_PAGE_URL

    def buy_without_login(self):
        self.click_btn(self._locators['make_order'])
        self.fill(self._locators['order_and_pay_enter_email'],'jk@wp.pl')
        self.fill(self._locators['order_and_pay_enter_phone'],'123456789')
        self.fill(self._locators['order_and_pay_enter_name'],'Jan')
        self.fill(self._locators['order_and_pay_enter_surname'],'Kowalski')
        self.fill(self._locators['order_and_pay_enter_street'],'Szeroka')
        self.fill(self._locators['order_and_pay_enter_number_of_house'],'44')
        self.fill(self._locators['order_and_pay_enter_city'],'Warszawa')
        self.fill(self._locators['order_and_pay_enter_codepost'],'11-001')
        self.click_btn(self._locators['order_and_pay_checkbox_required'])
        self.click_btn(self._locators['order_and_pay_the_last_step_order_and_pay'])

    def buy_with_login(self, email, password):
        self.click_btn(self._locators['make_order'])
        self.click_btn(self._locators['make_order_choice_my_account'])
        self.fill(self._locators['order_and_pay_enter_login_email'], email)
        self.fill(self._locators['order_and_pay_enter_login_password'], password)
        self.click_btn(self._locators['login_btn'])
        self.click_btn(self._locators['finalize_order'])
        self.fill(self._locators['order_and_pay_enter_phone'],'333-333-333')
        self.fill(self._locators['order_and_pay_enter_name'],'Anna')
        self.fill(self._locators['order_and_pay_enter_surname'],'Nowak')
        self.fill(self._locators['order_and_pay_enter_street'],'Cicha')
        self.fill(self._locators['order_and_pay_enter_number_of_house'],'13')
        self.fill(self._locators['order_and_pay_enter_city'],'Lublin')
        self.fill(self._locators['order_and_pay_enter_codepost'],'33-033')
        self.click_btn(self._locators['order_and_pay_checkbox_required'])
        self.click_btn(self._locators['order_and_pay_the_last_step_order_and_pay'])

    def buy_without_login_firm(self):
        self.click_btn(self._locators['make_order'])
        self.fill(self._locators['order_and_pay_enter_email'],'firma@wp.pl')
        self.fill(self._locators['order_and_pay_enter_phone'],'666.666.666')
        self.click_checkbox(self._locators['order_and_pay_by_firm_checkbox_invoice'])
        self.click_btn(self._locators['order_and_pay_choice_by_firm'])
        self.fill(self._locators['order_and_pay_by_firm_enter_firm_name'],'BigFirm')
        self.fill(self._locators['order_and_pay_enter_firm_nip'],'5840203593')
        self.fill(self._locators['order_and_pay_enter_name'],'Adam')
        self.fill(self._locators['order_and_pay_enter_surname'],'Nowak')
        self.fill(self._locators['order_and_pay_enter_street'],'Sucha')
        self.fill(self._locators['order_and_pay_enter_number_of_house'],'55')
        self.fill(self._locators['order_and_pay_enter_city'],'Warszawa')
        self.fill(self._locators['order_and_pay_enter_codepost'],'12-123')
        self.click_btn(self._locators['order_and_pay_checkbox_required'])
        self.click_btn(self._locators['order_and_pay_the_last_step_order_and_pay'])

    def successful_buy(self):
        element = self.find_element(self._locators['successful_buy'])
        message = element.text
        return message

