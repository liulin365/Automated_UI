from selenium import webdriver
import unittest
import read_config
import read_excel
import time

class test_login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = read_config.ReadConfig().get_http('baseurl')
        self.driver.maximize_window()

    def test_login_zc(self):
        u'''测试正向登录流程'''
        driver = self.driver
        driver.get(self.url)
        time.sleep(2)
        if driver.title == "医嘱综合点评分析系统":
            print("成功进入系统！")
        else:
            driver.refresh()
        try:
            driver.find_element_by_xpath("//*[@id='login-form']/div[1]/input").clear()
            driver.find_element_by_xpath("//*[@id='login-form']/div[1]/input").send_keys("admin")
            driver.find_element_by_xpath("//*[@id='login-form']/div[2]/input").clear()
            driver.find_element_by_xpath("//*[@id='login-form']/div[2]/input").send_keys("123")
            driver.find_element_by_id("btnLogin").click()
            time.sleep(2)
        except Exception as error:
            print(str(error))

    def tearDown(self):
        self.driver.quit()
        self.assertEqual()

if __name__ == '__main__':
    unittest.main()