from selenium.webdriver.common.by import By

REGISTRATION_LOCATORS = {
    'registration_form': {
        'email': {
            'by': By.ID,
            'value': 'b-email',
            'error_msg': {
                'by': By.CSS_SELECTOR,
                'value': 'label[for="b-email"] + div.form-hint'
            }
        },
        'password': {
            'by': By.ID,
            'value': 'b-password',
            'error_msg': {
                'by': By.CSS_SELECTOR,
                'value': 'label[for="b-password"] + div.form-hint'
            }
        },
        'rpassword': {
            'by': By.ID,
            'value': 'b-rpassword',
            'error_msg': {
                'by': By.CSS_SELECTOR,
                'value': 'label[for="b-rpassword"] + div.form-hint'
            }
        },
        'newsletter': {
            'by': By.ID,
            'value': 'check-nl-register',
            'error_msg': {
                'by': By.CSS_SELECTOR,
                'value': 'label[for="b-check-nl-register"] + div.form-hint'
            }

        },
        'terms_and_conditions': {
            'by': By.ID,
            'value': 'check-regshop',
            'error_msg': {
                'by': By.CSS_SELECTOR,
                'value': 'label[for="check-regshop"] + div.form-hint'
            }
        }
    },
    'submit_btn': {
        'by': By.CSS_SELECTOR,
        'value': 'button[class="confirm-button active-button"]'
    },
    'error_msgs': {
        'by': By.CSS_SELECTOR,
        'value': 'form  div.form-hint'
    },
    'registration_fail_msg': {
        'by': By.ID,
        'value': 'overallValidation'
    },
    'registration_success_msg': {
        'by': By.CSS_SELECTOR,
        'value': 'div.infobox-message'
    }
}