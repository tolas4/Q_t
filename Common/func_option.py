from configparser import ConfigParser
import os
from Common.func_address import option_dir

class ReadConf(ConfigParser):
    def __init__(self, file_path):
        super().__init__()
        self.read(file_path, encoding="utf-8")

conf = ReadConf(option_dir)