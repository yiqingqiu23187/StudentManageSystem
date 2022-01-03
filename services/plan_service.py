from services.base_service import BaseService
from dals.major_dal import MajorDAL
from dals.course_dal import CourseDAL
from dals.major_coure_relation_dal import MajorCourseRelationDAL

class PlanService(BaseService):
    def get_code(self):
        return 'p'

    def process(self, data):  # type: (str) -> None
        _, major_id, course_id, type = data.split()
        major = MajorDAL.query_by_id_or_name(major_id)
        if not major:
            raise Exception('专业不存在')
        course = CourseDAL.query_by_id_or_name(course_id)
        if not course:
            raise Exception('课程不存在')
        MajorCourseRelationDAL.new(major_id=major.id, course_id=course.id, type=int(type))

    def help(self):
        return '为某个专业指定培养计划，指令格式：p 专业id或名称 课程id或名称 课程类型\n' \
               '注：课程类型为 0:基础必修课 1:模块课 2:专业必修课 3:专业方向课 4:专业选修课'

