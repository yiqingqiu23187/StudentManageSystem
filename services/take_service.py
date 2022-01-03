from services.base_service import BaseService
from common.constants import CourseType
from dals.student_dal import StudentDAL
from dals.course_dal import CourseDAL
from dals.major_coure_relation_dal import MajorCourseRelationDAL
from dals.student_course_relation_dal import StudentCourseRelationDAL


class TakeService(BaseService):
    def get_code(self):
        return 't'

    def process(self, data):  # type: (str) -> None
        _, student_id, course_id, time = data.split()
        student = StudentDAL.query_by_id_or_name(student_id)
        if not student:
            raise Exception('学生不存在')
        course = CourseDAL.query_by_id_or_name(course_id)
        if not course:
            raise Exception('课程不存在')

        type = CourseType.any.value
        for major_course_relation in MajorCourseRelationDAL.instance_list:
            if major_course_relation.major_id == student.major_id and major_course_relation.course_id == course.id:
                type = major_course_relation.type
                break

        StudentCourseRelationDAL.new(student_id=student.id,
                                     course_id=course.id,
                                     time=time,
                                     type=type)

    def help(self):
        return '提交学生的课程修读结果，指令格式：t 学生id或姓名 课程id或名称 完成修读的时间'
