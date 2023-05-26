import logging

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from src.config.config_handler import ConfigHandler
from src.config.config_model import DriverType, ConfigData
from src.factory.chrome_factory import create_driver as create_chrome_driver
from src.factory.firefox_factory import create_driver as create_firefox_driver


# Mapping of driver type and create methods. For new driver supports, only add a new entry.
__BROWSER_FACTORIES = {
    DriverType.CHROME: create_chrome_driver,
    DriverType.FIREFOX: create_firefox_driver
}


def get_drivers(overwrite_config_path: str = None) -> tuple[WebDriver, WebDriverWait]:
    """Get web driver and wait driver instances.

    Default configuration is applied to the new instance of web driver, user have the option to
    override values in the configuration.

    :param overwrite_config_path: User custom configuration file
    :return: Web driver and wait driver instance.
    """
    logging.info("Initialize web driver")
    # Load configuration
    config_handler = ConfigHandler(overwrite_config_path)
    config = config_handler.load_config()

    # Create new driver using the configuration
    return __get_driver(config)


def __get_driver(config: ConfigData) -> tuple[WebDriver, WebDriverWait]:
    # Create driver
    logging.info(f"Create web driver instance, implicit wait: {config.implicit_wait}")
    driver = __BROWSER_FACTORIES[config.driver_type](config)

    # Configure implicit wait and maximize
    driver.implicitly_wait(config.implicit_wait)
    if config.maximize:
        logging.info("Maximize windows")
        driver.maximize_window()

    # Create web driver wait instance
    logging.info(f"Create web driver wait instance, explicit wait: {config.explicit_wait}")
    wait_driver = WebDriverWait(driver, config.explicit_wait)
    return driver, wait_driver
