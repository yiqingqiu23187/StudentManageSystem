from typing import List, Any

from dals.base_dal import BaseDAL
from models.student_course_relation import StudentCourseRelation


class StudentCourseRelationDAL(BaseDAL):
    model_class = StudentCourseRelation
    instance_list: list[StudentCourseRelation] = []
