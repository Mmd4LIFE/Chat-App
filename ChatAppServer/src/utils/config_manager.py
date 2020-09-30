"""
    created at sep 30/2020 by Mmd4LIFE
    - this package handle app configs
"""
from json import loads as json_loads
from easydict import EasyDict as edict

class ConfigManager:

    def __init__(self):
        self.config_path = "appsetings.json"