import os
import configparser
from Config import get_path

config = configparser.ConfigParser()
config_path = os.path.join(get_path.get_path(), 'Config', 'base_config.txt')
config.read(config_path , encoding='utf-8')

class ReadConfig():
    def get_http(self , parameter):
        value = config.get('HTTP' , parameter)
        return value

    def get_email(self , parameter):
        value = config.get('EMAIL' , parameter)
        return value

if __name__ == '__main__':
    test = ReadConfig()
    print(test.get_email('sender'))
