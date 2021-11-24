from xlrd import open_workbook
import json

booksdata = open_workbook(r"../params/data.xls")

jsondata = booksdata.sheet_by_index(0)

# print(jsondata)

# jsondata.cell_value(1, 0)
# print(jsondata.nrows)  # 行数
# print(jsondata.ncols)   # 列数

params_json = {}


def convert_data(path):
    for rows in range(jsondata.nrows):
        data1 = {}
        num1 = jsondata.cell_value(rows, 0)
        data1["type_text"] = jsondata.cell_value(rows, 1)
        data1["task_type"] = jsondata.cell_value(rows, 2)
        data1["title"] = jsondata.cell_value(rows, 3)
        data1["choosetime"] = jsondata.cell_value(rows, 4)
        data1["member"] = jsondata.cell_value(rows, 5)
        # "type_text": "任务管理", "task_type": "年度重点工作", "title": "2021年度重点工作", "choosetime": "2021,12,20", "member":
        # "杨冬,龚正勇"
        params_json[num1] = data1
    
    del params_json["用例标题"]
    # print(params_json)
    with open(path, "w", encoding='utf-8') as f1:  # r"../params/data.json"
        f1.write(json.dumps(params_json, indent=6, ensure_ascii=False))
    f1.close()
