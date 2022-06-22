from selenium.webdriver.common.by import By

PAYMENTS_LOCATORS = {
    'make_order': {
        'by': By.CSS_SELECTOR,
        'value': 'button.confirm-button:nth-child(2)'
    },
    'order_and_pay_enter_email': {
        'by': By.CSS_SELECTOR,
        'value': '#b-email'
    },
    'order_and_pay_enter_phone': {
        'by': By.CSS_SELECTOR,
        'value': '#b-phone'
    },
    'order_and_pay_enter_name': {
        'by': By.CSS_SELECTOR,
        'value': '#b-name'
    },
    'order_and_pay_enter_surname': {
        'by': By.CSS_SELECTOR,
        'value': '#b-subname'
    },
    'order_and_pay_enter_street': {
        'by': By.CSS_SELECTOR,
        'value': '#b-street'
    },
    'order_and_pay_enter_number_of_house': {
        'by': By.CSS_SELECTOR,
        'value': '#b-house'
    },
    'order_and_pay_enter_city': {
        'by': By.CSS_SELECTOR,
        'value': '#b-city'
    },
    'order_and_pay_enter_codepost': {
        'by': By.CSS_SELECTOR,
        'value': '#b-codepost'
    },
    'order_and_pay_checkbox_required': {
        'by': By.XPATH,
        'value': "//label[@for='check-regshop']"
    },
    'order_and_pay_the_last_step_order_and_pay': {
        'by': By.CSS_SELECTOR,
        'value': 'button.confirm-button:nth-child(2)'
    },
    'order_and_pay_choice_by_firm': {
        'by': By.CSS_SELECTOR,
        'value': 'div.check-simple:nth-child(3) > label:nth-child(2)'
    },
    'order_and_pay_by_firm_checkbox_invoice': {
        'by': By.CSS_SELECTOR,
        'value': '.checkbox-inline > label:nth-child(2)'
    },
    'order_and_pay_by_firm_enter_firm_name': {
        'by': By.CSS_SELECTOR,
        'value': '#b-company'
    },
    'order_and_pay_enter_firm_nip': {
        'by': By.CSS_SELECTOR,
        'value': '#b-nip'
    },
    'make_order_choice_my_account': {
        'by': By.CSS_SELECTOR,
        'value': '.checkout-tab > ul:nth-child(1) > li:nth-child(2)'
    },
    'order_and_pay_enter_login_email': {
        'by': By.ID,
        'value': 'login-login'
    },
    'order_and_pay_enter_login_password': {
        'by': By.ID,
        'value': 'login-password'
    },
    'login_btn': {
        'by': By.CSS_SELECTOR,
        'value': 'button.confirm-button:nth-child(4)'
    },
    'finalize_order': {
        'by': By.CSS_SELECTOR,
        'value': 'button.confirm-button:nth-child(2)'
    },
    'successful_buy': {
        'by': By.CSS_SELECTOR,
        'value': '#content > section > div.user-custom-content.headtxt'
    },

}
