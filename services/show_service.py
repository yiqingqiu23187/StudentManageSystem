from services.base_service import BaseService
from dals.student_dal import StudentDAL
from dals.major_dal import MajorDAL
from dals.course_dal import CourseDAL
from dals.major_coure_relation_dal import MajorCourseRelationDAL
from dals.student_course_relation_dal import StudentCourseRelationDAL
from dals.course_change_relation_dal import CoureChangeRelationDAL

class ShowService(BaseService):
    def get_code(self):
        return 's'

    def process(self, data):  # type: (str) -> None
        dals = [StudentDAL, MajorDAL, CourseDAL, MajorCourseRelationDAL, StudentCourseRelationDAL, CoureChangeRelationDAL]
        for dal in dals:
            print(dal.__name__)
            for instance in dal.instance_list:
                print(instance.__dict__)

    def help(self):
        return '查看当前所有db数据，指令格式：s'
