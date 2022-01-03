from dals.base_dal import BaseDAL
from models.major_course_relation import MajorCourseRelation

class MajorCourseRelationDAL(BaseDAL):
    model_class = MajorCourseRelation
    instance_list: list[MajorCourseRelation] = []
