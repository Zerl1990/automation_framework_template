import json
import os.path
import logging
import pathlib

from src.config.config_model import ConfigData


_DEFAULT_CONFIG_PATH = os.path.join(pathlib.Path(__file__).parent, "framework", "default_config.json")


class ConfigHandler:
    def __init__(self, overwrite_config_path: str = None):
        self.__overwrite_config_path = overwrite_config_path

    def load_config(self) -> ConfigData:
        """Load framework configuration data.

        :return: Dictionary with configuration values
        """
        default = self.__load_config(_DEFAULT_CONFIG_PATH)
        overwrite = self.__load_config(self.__overwrite_config_path)
        default.update(overwrite)
        config_data = ConfigData(default)
        logging.info(f"Framework configuration: {config_data}")
        return config_data

    @staticmethod
    def __load_config(config_path: str) -> dict:
        if config_path and os.path.exists(config_path):
            logging.info(f"Loading configuration from: {config_path}")
            with open(config_path) as config_file:
                return json.load(config_file)
        else:
            logging.warning(f"Config file not found {config_path}, ignoring configuration")
            return dict()
