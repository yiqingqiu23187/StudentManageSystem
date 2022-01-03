from services.base_service import BaseService
from dals.student_dal import StudentDAL
from dals.major_dal import MajorDAL
from dals.course_change_relation_dal import CoureChangeRelationDAL
from dals.student_course_relation_dal import StudentCourseRelationDAL
from dals.major_coure_relation_dal import MajorCourseRelationDAL
from common.constants import CourseType

class ChangeMajorService(BaseService):
    def get_code(self):
        return 'c'

    def help(self):
        return '学生转专业，指令格式：c 学生id或姓名 要转到的专业id或名称'

    def process(self, data):  # type: (str) -> None
        _, student_id, new_major_id = data.split()
        student = StudentDAL.query_by_id_or_name(student_id)
        if not student:
            raise Exception('学生不存在')
        new_major = MajorDAL.query_by_id_or_name(new_major_id)
        if not new_major:
            raise Exception('新专业不存在')

        student.major_id = new_major.id

        # 转专业时的课程转换，能转换的条件：1、对所有学生修读过的旧课，2、旧课能转化为一门新课，3、新课在新专业的需要修读的列表中
        src_dst_courses_map = {}
        for instance in CoureChangeRelationDAL.instance_list:
            src_dst_courses_map[instance.source_course_id] = instance.dest_coure_id
        for instance in StudentCourseRelationDAL.instance_list:
            if instance.student_id == student.id:
                type = CourseType.any.value
                if instance.course_id in src_dst_courses_map.keys():
                    for major_course_relation in MajorCourseRelationDAL.instance_list:
                        if major_course_relation.major_id == new_major.id and major_course_relation.course_id == src_dst_courses_map[instance.course_id]:
                            instance.source_course_id = instance.course_id
                            instance.course_id = src_dst_courses_map[instance.course_id]
                            type = major_course_relation.type
                            break
                instance.type = type

