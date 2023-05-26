import logging

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from src.config.config_model import ConfigData


def create_driver(config: ConfigData):
    """Create instance of chrome driver.

    :param config: Framework configuration.
    :return: Web driver instance to control Chrome browser.
    """
    logging.info("Initialize chrome driver")
    chrome_service = Service(config.drivers_path)
    chrome_options = webdriver.ChromeOptions()
    if config.incognito:
        logging.info("Enabled incognito mode")
        chrome_options.add_argument("--incognito")
    if config.headless:
        logging.info("Enabled headless mode")
        chrome_options.add_argument("--headless")
    return webdriver.Chrome(service=chrome_service, chrome_options=chrome_options)
