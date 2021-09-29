from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import pyautogui
wd= webdriver.Chrome()
wd.get('http://172.16.0.134:9012/minto/home')
wd.maximize_window()
wd.implicitly_wait(10)
wd.find_element_by_xpath('//*[@id="u34_input"]').send_keys('lih')
sleep(0.5)
wd.find_element_by_xpath('//*[@id="u35_input"]').send_keys('123456')
sleep(0.5)
wd.find_element_by_xpath('//*[@id="loginBut"]').click()
wd.implicitly_wait(10)
act = ActionChains(wd)
act.move_to_element(wd.find_element_by_xpath('//div[contains(text(),"任务管理")]')).perform()  #定位任务管理的
WebDriverWait(wd, 10).until(lambda x: x.find_element_by_xpath('//*[@title="年度重点工作"]'))  #定位年度重点
wd.find_element_by_xpath('//*[@title="年度重点工作"]').click()
sleep(2)
wd.switch_to.frame(1) #新建按钮的iframe
WebDriverWait(wd, 10).until(lambda x: x.find_element_by_xpath('//*[@title="新建事项"]'))
wd.find_element_by_xpath('//*[@title="新建事项"]').click()
sleep(2)
wd.switch_to.default_content()
wd.switch_to.frame(2)
wd.find_element_by_xpath('//*[@field_name="title"]').send_keys('这是任务名称')  #输入事项名称
wd.find_element_by_xpath('//*[@field_name="content"]').send_keys('这是任务名称')  #任务目标
wd.find_element_by_xpath('//*[@title="选择承办单位"]').click() #点击承办单位的框框
wd.switch_to.default_content()
wd.switch_to.frame(0) #选择机构的Iframe
'''做一个循环来读取承办人'''
member_list = ['李慧','杨冬','廖威']
for i in range(len(member_list)):
    sleep(1)
    wd.find_element_by_xpath('//*[@name="searchInput"]').clear()
    wd.find_element_by_xpath('//*[@name="searchInput"]').send_keys(member_list[i]) #输入承办人
    wd.find_element_by_xpath('//*[@title="立即查找"]').click() #搜索承办人
    wd.find_element_by_xpath('//*[@id="unitData1_extend_memberList"]/option').click() #点击选择承办人
wd.switch_to.default_content()
wd.find_element_by_xpath('//*[@value="确认"]').click()
wd.switch_to.default_content()
wd.switch_to.frame(2)
wd.find_element_by_xpath('//*[@show_type="date"]').click()
wd.switch_to.default_content()
wd.switch_to.frame(wd.find_element_by_xpath('//*[@class="mt-data-wrap mt-data-ans"]/iframe'))  #时间的Iframe
wd.find_element_by_xpath('//*[@id="dpTitle"]/div[4]/input').click()
wd.find_element_by_xpath('//*[@id="dpTitle"]/div[4]/input').send_keys('2021')#输入年份
wd.find_element_by_xpath('//*[@id="dpTitle"]/div[3]/input').click()
wd.find_element_by_xpath('//*[@id="dpTitle"]/div[3]/input').send_keys('12')#输入月份
wd.find_element_by_xpath('//td[contains(text(),"日")]').click()
wd.find_element_by_xpath('//*[@onclick="day_Click('+'2021,12,20'+');"]').click()
wd.find_element_by_xpath('//*[@value="确定"]')


