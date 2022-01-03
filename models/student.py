from models.base_model import BaseModel

class Student(BaseModel):
    def __init__(self, id=None, name=None, sex=None, major_id=None):
        super(Student, self).__init__(id)
        self.name = name
        self.sex = sex
        self.major_id = major_id

    # def __str__(self):
    #     return '学生id:%s 姓名:%s 性别:%s 专业:%s' % (self.id, self.name, self.sex, self.major_id)
