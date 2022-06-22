from selenium.webdriver.common.by import By


ITEM_LOCATORS = {
    'add_to_cart_btn': {
        'by': By.CSS_SELECTOR,
        'value': '.buy-button'
    },
    'go_to_cart_btn': {
        'by': By.CSS_SELECTOR,
        'value': 'a.confirm-button'
    },
    'return_btn': {
        'by': By.CSS_SELECTOR,
        'value': '.return-button'
    },
    'plus_btn': {
        'by': By.CSS_SELECTOR,
        'value': '.plus'
    },
    'add_few_product_btn': {
        'by': By.CSS_SELECTOR,
        'value': "#addproductamount"
    },
}