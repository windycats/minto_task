from minto_business.task_create import TaskCeate
import unittest
from selenium import webdriver
from time import *
import xlrd
from ddt import ddt, data, unpack, file_data


# time_data = ('任务管理,工作周报,第一周周报,2021，12，12,龚正勇')  # , '工作周报', '第一周周报', '2021，12，12', '龚正勇'
@ddt
class Case(unittest.TestCase, TaskCeate):
    def setUp(self) -> None:
        self.wd = webdriver.Chrome()
        self.wd.get('http://172.16.0.134:9012/minto/home')
        self.wd.maximize_window()
        self.wd.implicitly_wait(10)
        self.wd.find_element_by_xpath('//*[@id="u34_input"]').send_keys('lih')
        sleep(0.5)
        self.wd.find_element_by_xpath('//*[@id="u35_input"]').send_keys('123456')
        sleep(0.5)
        self.wd.find_element_by_xpath('//*[@id="loginBut"]').click()
        self.wd.implicitly_wait(10)
    
    @file_data('F:\python file\pythonProject\minto_task\params\data.json')
    def test_login(self, type_text, task_type, title, choosetime, member):
        # 添加新建的参数进行事项的创建
        self.naindu_create(type_text, task_type, title, choosetime, member)
        sleep(1)
        self.create_ok()
        sleep(1)
        self.wd.get_screenshot_as_file(
            'F:/python file/pythonProject/minto_task/test_report/screenshoot/' + title + '.jpg')
        sleep(1)
    def tearDown(self) -> None:
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
