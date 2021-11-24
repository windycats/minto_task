import unittest, time, os
from HTMLTestRunner import HTMLTestRunner


# 执行用例生成报告
def execute_case(reportpath):
    test_case = unittest.defaultTestLoader.discover(r'../minto_case', pattern='test_case.py')
    report_path = reportpath
    now = time.strftime('%Y_%m_%d_%H%M%S')
    file_name = report_path + '\\' + now + '测试报告.html'
    file_open = open(file_name, 'wb')
    runner = HTMLTestRunner(file_open, '测试报告', '报告详情')
    runner.run(test_case)
    file_open.close()


execute_case(r'F:\python file\pythonProject\minto_task\test_report\report')
