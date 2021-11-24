from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from time import *


class minto_element:
    def __init__(self, wd):
        self.wd = wd
        # self.wd = webdriver.Chrome()
    
    def click_element_byxapth(self, xpath):
        """直接通过xpath路径定位元素"""
        self.wd.find_element_by_xpath(xpath)
    
    def click_element_bytext(self, click_text):
        """任务管理下面的文本点击"""
        WebDriverWait(self.wd, 10).until(lambda x: x.find_element_by_xpath('//*[@title="' + click_text + '"]'))
        self.wd.find_element_by_xpath('//*[@title="' + click_text + '"]').click()
    
    def choose_tasktype(self, type_text, task_type):
        """选择任导航栏的事项类型"""
        act = ActionChains(self.wd)
        act.move_to_element(
            self.wd.find_element_by_xpath('//div[contains(text(),"' + type_text + '")]')).perform()  # 选择任务管理
        sleep(1)
        self.wd.find_element_by_xpath('//*[@title="' + task_type + '"]').click()
    
    def click_create(self):
        """点击新建"""
        self.wd.switch_to.frame(1)  # 新建按钮的iframe
        WebDriverWait(self.wd, 10).until(lambda x: x.find_element_by_xpath('//*[@title="新建事项"]'))
        self.wd.find_element_by_xpath('//*[@title="新建事项"]').click()
    
    def choose_time(self, input_time):
        """选择完成时间"""
        try:
            str1 = input_time.split(',')
            self.wd.switch_to.default_content()
            self.wd.switch_to.frame(2)
            self.wd.find_element_by_xpath('//*[@show_type="date"]').click()   # 点击触发时间窗口
            sleep(0.5)
            self.wd.switch_to.default_content()
            self.wd.switch_to.frame(
                self.wd.find_element_by_xpath('//*[@class="mt-data-wrap mt-data-ans"]/iframe'))  # 时间的Iframe
            self.wd.find_element_by_xpath('//*[@id="dpTitle"]/div[4]/input').click()
            self.wd.find_element_by_xpath('//*[@id="dpTitle"]/div[4]/input').send_keys(str1[0])  # 输入年份
            self.wd.find_element_by_xpath('//*[@id="dpTitle"]/div[3]/input').click()
            self.wd.find_element_by_xpath('//*[@id="dpTitle"]/div[3]/input').send_keys(str1[1])  # 输入月份
            self.wd.find_element_by_xpath('//td[contains(text(),"日")]').click()
        except Exception as e:
            print(e)
        try:
            
            self.wd.find_element_by_xpath('//*[@onclick="day_Click(' + input_time + ');"]').click()
            self.wd.find_element_by_xpath('//input[@id="dpOkInput"]').click()
        except Exception as e:
            print('{}时间组件的问题可以忽略报错'.format(e))      # 不同的事项类型用的时间字段不一样可以忽略异常
    
    def basic_info(self, title, choosetime, member, mubiao=None, xieban=None, leader=None, unit=None):
        """基本信息填写"""
        
        self.wd.switch_to.default_content()
        self.wd.switch_to.frame(2)
        self.wd.find_element_by_xpath('//input[@id="1"]').send_keys(title)  # 输入事项名称
        try:        # 用两个异常处理是因为当前页面存在三个承办单位的选项
            try:
                # self.wd.find_element_by_xpath('//*[@field_name="content"]').send_keys(mubiao)  # 任务目标
                self.wd.find_element_by_xpath('//*[@title="选择承办单位"]').click()  # 点击选择承办单位
            except :
                self.wd.find_element_by_xpath('//*[@title="选择责任单位"]').click()  # 点击选择责任单位
        except:
            self.wd.find_element_by_xpath('//*[@title="选择承办人员"]').click()  # 点击选择责任单位
        
        self.wd.switch_to.default_content()
        self.wd.switch_to.frame(0)  # 选择机构的Iframe
        '''做一个循环来读取承办人'''
        member_list = member.split(',')  # 输入的是字符串，用符号来切割一下
        print(len(member_list))
        # member_list = ['李慧', '杨冬', '廖威']
        for i in range(len(member_list)):
            sleep(1)
            self.wd.find_element_by_xpath('//*[@name="searchInput"]').clear()
            self.wd.find_element_by_xpath('//*[@name="searchInput"]').send_keys(member_list[i])  # 输入承办人
            self.wd.find_element_by_xpath('//*[@title="立即查找"]').click()  # 搜索承办人
            self.wd.find_element_by_xpath('//*[@id="unitData1_extend_memberList"]/option').click()  # 点击选择承办人
        self.wd.switch_to.default_content()

        self.wd.find_element_by_xpath('//*[@value="确认"]').click()
        self.choose_time(choosetime)  # 输入时间
        
        sleep(1)
    
    def create_ok(self):
        """点击交办"""
        self.wd.switch_to.default_content()
        self.wd.switch_to.frame(2)
        self.wd.find_element_by_xpath('//span[contains(text(),"交办")]').click()
