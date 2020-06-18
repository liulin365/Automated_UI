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
    excel_sheet = open_excel.sheet_by_name("Sheet1")
    # 获取这个Sheet中内容的行数
    lines = excel_sheet.nrows
    # 循环取值，排除标题无用数据等
    for line in range(lines):
        if excel_sheet.row_values(line)[0] != "case_name":
            cls.append(excel_sheet.row_values(line))
    return cls

# 写入excel文件
def write_excel():
    myWorkbook = xlwt.Workbook()
    # 数据格式
    myStyle = xlwt.easyxf('font: name Times New Roman, color-index red, bold on', num_format_str='#,##0.00')
    mySheet.write(i, j, 1234.56, myStyle)
    # 写入A3，数值等于1
    mySheet.write(2, 0, 1)
    #保存
    myWorkbook.save('excelFile.xls')

# 修改excel文件


if __name__ == '__main__':
    get_excel("case_1.xlsx")


