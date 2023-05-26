import logging

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from src.page_objects.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver: WebDriver, wait_driver: WebDriverWait):
        super(LoginPage, self).__init__(driver, wait_driver)

    def login(self, email: str, password: str):
        logging.info(f"Login with email address {email} and password *****")
        self.element("email_input").wait_clickable().send_keys(email)
        self.element("password_input").wait_clickable().send_keys(password)
        self.element("login_btn").wait_clickable().click()

    def get_warning_message(self):
        return self.element("warning_message").wait_visible().text
