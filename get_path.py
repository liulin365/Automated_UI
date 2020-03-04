import os

def get_path():
    path = os.path.join(os.getcwd())
    return path

if __name__ == '__main__':
    print(str("当前路径为：" + get_path()))