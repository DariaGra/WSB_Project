from pages.base_page import BasePage
from config import ITEM_PAGE_URL
from pages.item_page.selectors import ITEM_LOCATORS


class ItemPage(BasePage):
    _locators = ITEM_LOCATORS
    _url = ITEM_PAGE_URL

    def __init__(self, driver):
        super().__init__(driver)
        self.go_to(self._url)

    def add_item_to_cart(self):
        self.click_btn(self._locators['add_to_cart_btn'])
        self.click_btn(self._locators['go_to_cart_btn'])

    def add_two_items_to_cart(self):
        self.click_btn(self._locators['plus_btn'])
        self.add_item_to_cart()

    def add_again_the_same_item(self):
        self.click_btn(self._locators['add_to_cart_btn'])
        self.go_to(self._url)
        self.add_item_to_cart()

    def add_100_same_items(self):
        self.clear(self._locators['add_few_product_btn'])
        self.fill(self._locators['add_few_product_btn'], '100')
        self.click_btn(self._locators['add_to_cart_btn'])
        self.click_btn(self._locators['go_to_cart_btn'])

    def add_999_items(self):
        self.clear(self._locators['add_few_product_btn'])
        self.fill(self._locators['add_few_product_btn'], '999')
        self.click_btn(self._locators['add_to_cart_btn'])

    def click_go_to_cart_button(self):
        self.click_btn(self._locators['go_to_cart_btn'])
