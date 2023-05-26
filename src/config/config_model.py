import os
import pathlib
from enum import Enum


class DriverType(Enum):
    """
    List of valid and accepted driver types.
    """
    CHROME = "chrome"
    FIREFOX = "firefox"

    @classmethod
    def from_name(cls, name):
        try:
            return cls(name)
        except:
            raise ValueError(f"Invalid browser name: {name}")


class ConfigData:
    """
    Abstraction to control config data access
    """
    def __init__(self, config_dict: dict):
        self.__config_dict = config_dict
        self.__driver_type = None
        self.__implicit_wait = None
        self.__explicit_wait = None
        self.__driver_path = None
        self.__headless = None
        self.__incognito = None
        self.__maximize = None
        self.__headless_resolution = None

    @property
    def driver_type(self) -> DriverType:
        browser_name = self.__config_dict["browser_name"]
        return DriverType.from_name(browser_name)

    @property
    def implicit_wait(self) -> int:
        implicit_wait = self.__config_dict["implicit_wait"]
        implicit_wait_type = type(implicit_wait)
        if implicit_wait_type is not int:
            raise TypeError(f"Invalid type for implicit wait: {implicit_wait_type}")
        if implicit_wait < 0:
            implicit_wait = 0
        return implicit_wait

    @property
    def explicit_wait(self) -> int:
        explicit_wait = self.__config_dict["explicit_wait"]
        explicit_wait_type = type(explicit_wait)
        if explicit_wait_type is not int:
            raise TypeError(f"Invalid type for explicit wait: {explicit_wait_type}")
        if explicit_wait < 0:
            explicit_wait = 0
        return explicit_wait

    @property
    def drivers_path(self) -> str:
        drivers_path = self.__config_dict["drivers_path"]
        absolute_path = os.path.join(pathlib.Path(__file__).parent.parent.parent, *drivers_path.split("/"))
        if not os.path.exists(absolute_path):
            raise FileNotFoundError(f"Drivers path not found: {absolute_path}")
        return absolute_path

    @property
    def headless_resolution(self) -> tuple:
        width = self.__config_dict["headless"]["resolution"]["width"]
        height = self.__config_dict["headless"]["resolution"]["height"]
        return width, height

    @property
    def maximize(self) -> bool:
        return self.__config_dict["maximize"]

    @property
    def headless(self) -> bool:
        return self.__config_dict["headless"]["enabled"]

    @property
    def incognito(self) -> bool:
        return self.__config_dict["incognito"]

    def __str__(self):
        return str(self.__config_dict)
