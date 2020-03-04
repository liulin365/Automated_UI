import read_config
import get_path
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

#找出Report下最新的报告
def find_new_email():
    lists = os.listdir(report_path)
    lists.sort(key=lambda fn: os.path.getmtime(report_path + "\\" + fn) if not
    os.path.isdir(report_path + "\\" + fn) else 0)
    # print('最新的文件为： ' + lists[-1])
    file_name = lists[-1]
    file_path = os.path.join(report_path, lists[-1])
    # print(file)
    return file_path , file_name

# 发送最新的报告
def send_email(file_path,file_name):
    # 创建一个带附件的实例
    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = subject
    # 邮件正文内容
    message.attach(MIMEText('WebUI自动化测试', 'plain', 'utf-8'))
    # 构造附件
    att1 = MIMEText(open(file_path, 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att1["Content-Disposition"] = f"attachment; filename={file_name}.html"
    message.attach(att1)
    try:
        smtp = SMTP(smtp_server, smtp_port)
        smtp.login(sender, password)
        smtp.sendmail(sender, recipient, message.as_string())
        # print("邮件已发送！")
    except(Exception) as Error:
        # print(Error+"邮件发送失败！")
        pass
    finally:
        smtp.quit()

if __name__ == '__main__':
    a , b = find_new_email()
    send_email(a,b)