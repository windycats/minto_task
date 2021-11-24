from minto_business.task_create import TaskCreate
import unittest
from selenium import webdriver
from time import *
from convert_data.excel_json import convert_data
from ddt import ddt, data, unpack, file_data


# time_data = ('任务管理,工作周报,第一周周报,2021，12，12,龚正勇')  # , '工作周报', '第一周周报', '2021，12，12', '龚正勇'
@ddt
class Case(unittest.TestCase, TaskCreate):
    def setUp(self) -> None:
        """打开一个网址和登陆网址"""
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
        try:
            self.wd.find_element_by_xpath(
                '/html/body/div[3]/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td/div[2]/input[2]').click()
        except :
            pass
        convert_data(r'../params.data.json')
    
    @file_data(r'../params.data.json')  # 引用ddt参数
    def test_login(self, type_text, task_type, title, choosetime, member):
        """ 添加新建的参数进行事项的创建"""
        self.naindu_create(type_text, task_type, title, choosetime, member)  # 调用新建业务
        # self.create_ok()  # 确认创建
        sleep(1)
        self.wd.get_screenshot_as_file(
            'F:/python file/pythonProject/minto_task/test_report/screenshoot/' + title + '.jpg')  # 创建事项后截图存留
    
    def tearDown(self) -> None:
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
