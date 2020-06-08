import os

def get_path():
    # 这个是获取当前文件的上一级目录
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return path

if __name__ == '__main__':
    print(str("当前路径为：" + get_path()))
