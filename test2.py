import xlrd

data = xlrd.open_workbook('./params/data.xls')
print(data.sheets())
# table = data.sheet_by_name('任务管理')
table = data.sheet_by_index(0)
# print(table.nrows,table.ncols)
print(table.cell(1, 0))
print(table.cell(1, 1))
print(table.cell(1, 2))
print(table.cell(1, 3))
print(table.cell(1, 4))
task = []
for i in range(table.nrows-1):
    type= table.cell(i+1, 0).value
    task.append(type)
    task_type= table.cell(i+1, 1).value
    task.append(task_type)
    task_name= table.cell(i+1, 2).value
    task.append(task_name)
    task_time= table.cell(i+1, 3).value
    task.append(task_time)
    task_member= table.cell(i+1, 4).value
    task.append(task_member)
print(task)
