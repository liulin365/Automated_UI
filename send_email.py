import read_config
from Config import get_path
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP

report_path = os.path.join(get_path.get_path(), 'Report')
sender = read_config.ReadConfig().get_email('sender')
recipient = read_config.ReadConfig().get_email('recipient')
cc = read_config.ReadConfig().get_email('cc')
subject = read_config.ReadConfig().get_email('subject')
smtp_server = read_config.ReadConfig().get_email('smtp_server')
smtp_port = read_config.ReadConfig().get_email('smtp_port')
password = read_config.ReadConfig().get_email('password')

# 找出Report下最新的报告
def find_new_email():
    # 列表形式返回
    lists = os.listdir(report_path)
    # 以修改时间来排序
    lists.sort(key = lambda fn : os.path.getmtime(report_path))
    file_name = lists[-1]
    file_path = os.path.join(report_path, lists[-1])
    return file_path , file_name

# 制作邮件
def make_email():
    file_path , file_name = find_new_email()
    # 创建一个带附件的实例
    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = subject
    # 邮件正文内容
    message.attach(MIMEText('接口自动化测试报告', 'plain', 'utf-8'))
    # 构造附件
    att1 = MIMEText(open(file_path, 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att1["Content-Disposition"] = f"attachment; filename = {file_name}接口测试报告.html"
    message.attach(att1)
    return message

# 发送最新的邮件
def send_email():
    try:
        message = make_email()
        smtp = SMTP(smtp_server, smtp_port)
        smtp.login(sender, password)
        smtp.sendmail(sender, recipient, message.as_string())
        print("邮件已发送！")
    except(Exception) as Error:
        print("邮件发送失败！")
        print(str(error))
        print("错误文件：" + error.__traceback__.tb_frame.f_globals["__file__"])
        print("错误行数：" + error.__traceback__.tb_lineno)
    finally:
        smtp.quit()


if __name__ == '__main__':
    send_email()