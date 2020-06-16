import os
import shutil

def listdir(path , list_name): #传入存储的list
    for file in os.listdir(path):
        file_path = os.path.join(path , file)
        if os.path.isdir(file_path):
            listdir(file_path , list_name)
        else:
            list_name.append((file_path , os.path.getctime(file_path)))

def newestfile(target_list):
    newest_file = target_list[0]
    for i in range(len(target_list)):
        if i < (len(target_list)-1) and newest_file[1] < target_list[i+1][1]:
            newest_file = target_list[i+1]
        else:
            continue
    print('newest file is' , newest_file)
    return newest_file

p = r'D:\python_project\Interface\Test_File'
list = []
listdir(p, list)
new_file = newestfile(list)
print('from:',new_file[0])
print('to:',shutil.copy(new_file[0], 'C:\\Users\\Administrator\\Desktop\\img\\a.xml'))

if __name__ == '__main__':
    # get_all("D:\python_project\Interface\Test_File")
    # print(result)
    get_dir = os.listdir("D:\python_project\Interface\Test_File")
    print(get_dir)