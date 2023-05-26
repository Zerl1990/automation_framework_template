import logging

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from src.page_objects.base_page import BasePage


class AccountPage(BasePage):
    def __init__(self, driver: WebDriver, wait_driver: WebDriverWait):
        super(AccountPage, self).__init__(driver, wait_driver)

    def get_right_menu_names(self) -> list[str]:
        logging.info("Get right menu names")
        self.element("right_menu_options").wait_visible()
        return [element.text for element in self.element("right_menu_options").find_elements()]

    def click_right_menu(self, name: str):
        logging.info(f"click right menu {name}")
        self.element("right_menu_options").wait_visible()
        elements = self.element("right_menu_options").find_elements()
        for element in elements:
            if element.text == name:
                logging.info(f"Right menu found {name}")
                element.click()
                break
        else:
            error_msg = f"Right menu is not visibile: {name}"
            logging.error(error_msg)
            raise RuntimeError(error_msg)


