from dals.base_dal import BaseDAL
from models.course import Course


class CourseDAL(BaseDAL):
    model_class = Course
    instance_list = []
