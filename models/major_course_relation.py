# 专业与课程的联系集，代表该专业需要上这门课
# type 课程类型，见CourseType
from models.base_model import BaseModel


class MajorCourseRelation(BaseModel):
    def __init__(self, id=None, major_id=None, course_id=None, type=None, direction=None):
        super(MajorCourseRelation, self).__init__(id)
        self.type = type
        self.course_id = course_id
        self.major_id = major_id
        self.direction = direction
