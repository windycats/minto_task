from minto_basic.basic_element import minto_element


class TaskCeate(minto_element):
    def naindu_create(self, type_text, task_type, title, choosetime, member):
        self.choose_tasktype(type_text, task_type)
        self.click_create()
        self.basic_info(title, choosetime, member)
