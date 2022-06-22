from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def go_to(self, url):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    def find_element(self, locator, wait=20):
        element = WebDriverWait(self.driver, wait).until(ec.presence_of_element_located((locator['by'], locator['value'])))
        return element

    def find_elements(self, locator):
        elements = self.driver.find_elements(by=locator['by'], value=locator['value'])
        return elements

    def fill(self, locator, value='', wait=20):
        element = WebDriverWait(self.driver, wait).until(ec.presence_of_element_located((locator['by'], locator['value'])))
        element.send_keys(value)

    def click_btn(self, locator, wait=20):
        btn = WebDriverWait(self.driver, wait).until(ec.element_to_be_clickable((locator['by'], locator['value'])))
        btn.click()

    def click_checkbox(self, locator, selected=False):
        if selected:
            btn = self.driver.find_element(locator['by'], locator['value'])
            self.driver.execute_script("arguments[0].click();", btn)

    def get_message(self, locator, wait=10):
        element = WebDriverWait(self.driver, wait).until(ec.presence_of_element_located((locator['by'], locator['value'])))
        msg = element.text
        return msg

    def clear(self, locator):
        element = self.driver.find_element(locator['by'], locator['value'])
        element.clear()


