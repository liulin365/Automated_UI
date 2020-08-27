import os
import xlwt
import xlrd3
from Config import get_path

# 获取excel的路径
def get_excel_path(excel_name):
    excel_name_path = os.path.join(get_path.get_path(), 'Test_File', excel_name)
    return excel_name_path

# 读取excel文件
def get_excel(excel_name):
    cls = []
    # 打开excel并保存内容至open_excel
    open_excel = xlrd3.open_workbook(get_excel_path(excel_name))
    # 打开指定Sheet的内容保存至excel_sheet
    excel_sheet_main = open_excel.sheet_by_name("Sheet1")
    # 获取这个Sheet中内容的行数
    lines = excel_sheet_main.nrows
    # 循环取值，排除标题无用数据等
    for line in range(lines):
        if excel_sheet_main.row_values(line)[0] != "case_name":
            cls.append(excel_sheet_main.row_values(line))
    return cls

# 写入excel文件




if __name__ == '__main__':
    get_excel("case_1.xlsx")


