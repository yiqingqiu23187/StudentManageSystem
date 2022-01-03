# 课程之间可以转换的联系集
from models.base_model import BaseModel


class CoureChangeRelation(BaseModel):
    def __init__(self, id=None, source_course_id=None, dest_coure_id=None):
        super(CoureChangeRelation, self).__init__(id)
        self.dest_coure_id = dest_coure_id
        self.source_course_id = source_course_id
