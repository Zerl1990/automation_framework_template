import json
import logging
import os
import pathlib

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from src.web_elements.common import WebElementWrapper


_LOCATOR_DIR_PATH = os.path.join(pathlib.Path(__file__).parent.parent.parent, "locators")


class BasePage:
    def __init__(self, driver: WebDriver, wait_driver: WebDriverWait):
        self.__driver = driver
        self.__wait_driver = wait_driver
        self.__load_locators_attributes()

    def open(self):
        self.__driver.get(self.url)

    def close(self):
        self.__driver.close()

    def get_title(self) -> str:
        return self.__driver.title

    def get_url(self) -> str:
        return self.__driver.current_url

    def element(self, key_name) -> WebElementWrapper:
        return self.__dict__[key_name]

    def __load_locators_attributes(self):
        locator_config = self.__load_locators_config()
        logging.info(f"Locators config: {locator_config}")
        self.__dict__["url"] = locator_config["url"]
        logging.info(f"Adding url instance variable: {locator_config['url']}")
        for key, val in locator_config["locators"].items():
            if val["by"] not in By.__dict__.keys():
                raise ValueError(f"Locator {key} has invalid by value: {val['by']}")
            by = By.__dict__[val["by"]]
            logging.info(f"Adding {key} instance variable, by: {by}, value: {val['value']}")
            self.__dict__[key] = WebElementWrapper(self.__driver, self.__wait_driver, by, val["value"])

    def __load_locators_config(self):
        locator_file_name = type(self).__name__
        locator_absolute_path = os.path.join(_LOCATOR_DIR_PATH, locator_file_name + ".json")
        logging.info(f"Loading locators for class {locator_file_name} from {locator_absolute_path}")
        if not os.path.exists(locator_absolute_path):
            raise FileNotFoundError(f"Locator not found: {locator_absolute_path}")
        with open(locator_absolute_path) as locators_file:
            return json.load(locators_file)
