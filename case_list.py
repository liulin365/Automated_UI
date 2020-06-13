# 这个文件主要用来选择需要的用例文件
from Test_File import *
from Config import get_path
import os

file_path = os.path.join(get_path() , 'Test_File')
get_dir = os.listdir(file_path)
def file_list():
    user_choose_file = []
    print("以下为可执行的用例文件：")
    print(get_dir)
    print("请输入需要执行的用例文件:")
    user_input = input("")
    user_choose_file.append(user_input)
    return user_choose_file

if __name__ == '__main__':
    print(file_list())