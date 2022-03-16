from minto_basic.basic_element import minto_element


class TaskCreate(minto_element):
    def naindu_create(self, type_text, task_type, title, choosetime, member):
        """任务管理的业务"""
        self.choose_tasktype(type_text, task_type)  # 选择事项类型和任务类型
        self.click_create()     # 点击创建
        self.basic_info(title, choosetime, member)  # 点击标题、时间、承办人三个必填项
        self.create_ok()    # 点击交办

