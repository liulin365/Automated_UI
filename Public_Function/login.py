from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()

def login():
    driver.get("http://10.158.5.246:8090/adviceAnalysis/views/login/login.jsp")
    sleep(1)

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
        sleep(2)
    except Exception as error:
        print(str(error))
        print(error.__traceback__.tb_frame.f_globals["__file__"])
        print(error.__traceback__.tb_lineno)


if __name__ == '__main__':
    login()
    driver.quit()