import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from helpers import generate_unique_email_and_tag
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from pages.registration_page.registration_page import RegistrationPage


@pytest.fixture(scope='session')
def driver_instance():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.close()


@pytest.fixture(scope='class')
def setup_test_base(request, create_registered_user, driver_instance):
    driver = driver_instance
    request.cls.login_email, request.cls.login_password = create_registered_user
    request.cls.driver = driver


@pytest.fixture(scope='class')
def set_email_and_tag_attribute(request):
    new_email, tag = generate_unique_email_and_tag()
    request.cls.email = new_email
    request.cls.tag = tag


@pytest.fixture(scope='session')
def create_registered_user():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    user = RegistrationPage(driver)
    login_password = 'Test123!'
    login_email, tag = generate_unique_email_and_tag()
    user.register_with(
        email=login_email,
        password=login_password,
        rpassword=login_password,
        newsletter=False,
        terms_and_conditions=True
    )
    user.confirm_email(login_email, tag)
    driver.close()
    return login_email, login_password
