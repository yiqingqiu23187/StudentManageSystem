# 学生与课程的联系集，代表该学生上过这门课
# type 课程类型，见CourseType
from models.base_model import BaseModel


class StudentCourseRelation(BaseModel):
    def __init__(self, id=None, student_id=None, course_id=None, source_course_id=None, time=None, type=None):
        super(StudentCourseRelation, self).__init__(id)
        self.student_id = student_id
        self.course_id = course_id
        self.source_course_id = source_course_id
        self.time = time
        self.type = type
