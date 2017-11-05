#coding:utf-8
from glob import *
import xlwt
import xlrd
import os

# 将dir改为xlsx的存储目录路径
# dir = r'C:\Users\Max Wang\Desktop\xlsx'
dir = os.getcwd()
headers = ['学院', '姓名', '学号', '民族', '校区', '宿舍楼', '宿舍号', '联系方式', '留校原因', '留校时间']
# 获取目录下xlsx名
xlsx_list = []
for name in glob(dir + r'\*.xlsx'):
    xlsx_list.append(name)

print 'I will join the following xlsx,  %d in sum' % len(xlsx_list)
for name in xlsx_list:
    print name
# 读取xlsx内容
contents = []
for name in xlsx_list:
    workbook = xlrd.open_workbook(name)
    sheet = workbook.sheet_by_name('Sheet1')
    contents.append(sheet.row_values(1))

# print contents
# 将读取数据写入output.xlsx
output = xlwt.Workbook(encoding = 'utf-8')
sheet = output.add_sheet(u'Sheet1')
# 填入表头
for i in range(len(headers)):
    sheet.write(0, i, headers[i])

# 填入数据
for j in range(len(contents)):
    row = contents[j]
    for i in range(len(row)):
        sheet.write(j + 1, i, row[i])

output.save(u'output.xls')
print 'join completed successfully!'