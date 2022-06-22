from selenium.webdriver.common.by import By

CART_LOCATORS = {
    'clear_cart_btn': {
        'by': By.CSS_SELECTOR,
        'value': '.clear-cart'
    },
    'remove_btn': {
        'by': By.CSS_SELECTOR,
        'value': '.removepos'
    },
    'cart_btn': {
        'by': By.CSS_SELECTOR,
        'value': '#cart-box > span:nth-child(1)'
    },
    'empty_cart_msg': {
        'by': By.CSS_SELECTOR,
        'value': '.infobox-headline'
    },
    'plus_btn_2': {
        'by': By.CSS_SELECTOR,
        'value': '.plus'
    },
    'item_in_cart': {
        'by': By.CSS_SELECTOR,
        'value': '.productcart-info > a:nth-child(1)'
    },
    'price_of_one_item': {
        'by': By.CSS_SELECTOR,
        'value': '.price > strong:nth-child(2)'
    },
    'value': {
        'by': By.CSS_SELECTOR,
        'value': '.value-items > strong:nth-child(1)'
    },
    'cart_value': {
        'by': By.XPATH,
        'value': "//input[@type='tel']"
    },
    'cart': {
        'by': By.CSS_SELECTOR,
        'value': '#cart-box > span:nth-child(1)'
    },
    'count': {
        'by': By.CSS_SELECTOR,
        'value': '.recalculate-all'
    },
    'back_to_shopping': {
        'by': By.CSS_SELECTOR,
        'value': '.cart-back-link'
    },
    'back_url': {
        'by': By.CSS_SELECTOR,
        'value': '.main-greeting-headline'
    },
    'minus': {
        'by': By.CSS_SELECTOR,
        'value': '.minus'
    },
}