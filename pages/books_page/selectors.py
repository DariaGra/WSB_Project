from selenium.webdriver.common.by import By

BOOKS_LOCATORS = {
    'book_price': {
        'by': By.CLASS_NAME,
        'value': 'product-price '
    },
    'max_price': {
        'by': By.CSS_SELECTOR,
        'value': '#filter-price2'
    },
    'min_price': {
        'by': By.CSS_SELECTOR,
        'value': '#filter-price1'
    },
    'filter_enabled': {
        'by': By.CSS_SELECTOR,
        'value': '.single-pill > span:nth-child(1) > b:nth-child(1)'
    },
    'sorter_button': {
        'by': By.CSS_SELECTOR,
        'value': '.sorter-button'
    },
    'price_desc': {
        'by': By.CSS_SELECTOR,
        'value': '.sorter-listing > span:nth-child(4) > label:nth-child(2)'
    },
    'price_asc': {
        'by': By.CSS_SELECTOR,
        'value': '.sorter-listing > span:nth-child(3) > label:nth-child(2)'
    },
    'book_title': {
        'by': By.CLASS_NAME,
        'value': 'product-name'
    },
    'name_desc': {
        'by': By.CSS_SELECTOR,
        'value': '.sorter-listing > span:nth-child(2) > label:nth-child(2)'
    },
    'name_asc': {
        'by': By.CSS_SELECTOR,
        'value': '.sorter-listing > span:nth-child(1) > label:nth-child(2)'},
}