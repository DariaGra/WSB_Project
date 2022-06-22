from pages.base_page import BasePage
from config import CART_PAGE_URL
from pages.cart_page.selectors import CART_LOCATORS


class CartPage(BasePage):
    _locators = CART_LOCATORS
    _url = CART_PAGE_URL

    def go_to_empty_cart(self):
        self.click_btn(self._locators['cart'])
        empty_cart = self.find_element(self._locators['empty_cart_msg']).text
        return empty_cart

    def check_that_item_is_in_cart(self):
        item = self.find_element(self._locators['item_in_cart']).text
        return item

    def plus_one_item(self):
        self.click_btn(self._locators['plus_btn_2'])

    def remove_item(self):
        self.click_btn(self._locators['remove_btn'])

    def clear_cart(self):
        self.click_btn(self._locators['clear_cart_btn'])

    def check_how_many_items_are_in_cart(self):
        element = self.find_element(self._locators['cart_value'])
        items = element.get_attribute('value')
        return items

    def check_that_cart_is_empty(self):
        empty_cart = self.find_element(self._locators['empty_cart_msg']).text
        return empty_cart

    def recalculate_cart(self):
        self.click_btn(self._locators['count'])

    def change_the_number_of_items_in_cart_to_5(self):
        self.clear(self._locators['cart_value'])
        self.fill(self._locators['cart_value'], '5')

    def back_to_shopping(self):
        self.click_btn(self._locators['back_to_shopping'])

    def back_url(self):
        element = self.find_element(self._locators['back_url'])
        start = element.text
        return start

    def minus_one_item(self):
        self.click_btn(self._locators['minus'])