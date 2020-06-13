import os

result = []

def get_all(cwd):
    get_dir = os.listdir(cwd)
    for i in get_dir:
        sub_dir = os.path.join(cwd , i)
        if os.path.isdir(sub_dir):
            get_all(sub_dir)
        else:
            result.append(i)

if __name__ == '__main__':
    # get_all("D:\python_project\Interface\Test_File")
    # print(result)
    get_dir = os.listdir("D:\python_project\Interface\Test_File")
    print(get_dir)