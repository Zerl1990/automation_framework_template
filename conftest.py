import pytest

from src.factory.webdriver_factory import get_drivers


@pytest.fixture(autouse=True)
def web_drivers():
    driver, wait_driver = get_drivers()
    yield driver, wait_driver
    driver.quit()

