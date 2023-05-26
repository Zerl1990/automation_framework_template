import logging

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from src.config.config_model import ConfigData


def create_driver(config: ConfigData):
    """Create instance of chrome driver.

    :param config: Framework configuration.
    :return: Web driver instance to control Firefox browser.
    """
    logging.info("Initialize firefox driver")
    service = Service(config.drivers_path)
    ff_options = webdriver.FirefoxOptions()
    ff_profile = webdriver.FirefoxProfile()
    ff_profile.set_preference("browser.privatebrowsing.autostart", config.headless)
    ff_options.headless = config.headless
    logging.info(f"Set private browsing: {config.headless}")
    logging.info(f"Set headless mode: {config.headless}")
    return webdriver.Firefox(service=service, options=ff_options, firefox_profile=ff_profile)
