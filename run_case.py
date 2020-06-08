import unittest
import HTMLTestRunner
import os
from Config import get_path
import time
import send_email
# import case_list

#构造测试套件方法
def creatsuit():
    testunit = unittest.TestSuite()
    #查找目录下的测试文件
    case_path = os.path.join(get_path.get_path(), 'Test_Case')
    discover = unittest.defaultTestLoader.discover(case_path , pattern = 'test_*.py' , top_level_dir = None)
    #将测试用例加入到测试套件中
    # test_case_list = case_list.case_list()
    for test_suit in discover:
        for test_case in test_suit:
            testunit.addTests(test_case)
    return testunit

alltestnames = creatsuit()

# #手动选择需要执行的用例
# #将用例组装数组
# alltestnames = [case_list.test_1.Baidu,case_list.test_2.Youdao]
# #创建测试套件
# testunit = unittest.TestSuite()
# #循环读取数组中的用例
# for test in alltestnames:
#     testunit.addTest(unittest.makeSuite(test))

#生成并写入报告
now = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime(time.time()))
report_path = os.path.join(get_path.get_path(), 'Report')
file_name = os.path.join(report_path ,'result_' + now + '.html')
fp = open(file_name , 'wb')
runner = HTMLTestRunner.HTMLTestRunner(stream = fp,description = '测试结果',title = '我的测试报告')

#执行测试套件
runner.run(alltestnames)
fp.close()

#发送邮件
try:
    a , b = send_email.find_new_email()
    send_email.send_email(a, b)
    print("邮件已发送！")
except Exception as error:
    print("邮件发送失败！")
    print(str(error))
    print("错误文件：" + error.__traceback__.tb_frame.f_globals["__file__"])
    print("错误行数：" + error.__traceback__.tb_lineno)