import os
import configparser
import get_path

config = configparser.ConfigParser()
config_path = os.path.join(get_path.get_path() ,'Config' , 'base_config.txt')
config.read(config_path , encoding='utf-8')

class ReadConfig():
    def get_http(self , name):
        value = config.get('HTTP' , name)
        return value

    def get_email(self , name):
        value = config.get('EMAIL' , name)
        return value

if __name__ == '__main__':
    AAAA = ReadConfig()
    print(AAAA.get_email('sender'))
