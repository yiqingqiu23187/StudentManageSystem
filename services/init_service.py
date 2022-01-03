from services.base_service import BaseService
from dals.student_dal import StudentDAL
from dals.major_dal import MajorDAL
from dals.course_dal import CourseDAL
from dals.major_coure_relation_dal import MajorCourseRelationDAL
from dals.student_course_relation_dal import StudentCourseRelationDAL
from dals.course_change_relation_dal import CoureChangeRelationDAL
from common.constants import CourseType


class InitService(BaseService):
    def get_code(self):
        return 'i'

    def process(self, data):  # type: (str) -> None
        # 重新初始化
        dals = [StudentDAL, MajorDAL, CourseDAL, MajorCourseRelationDAL, StudentCourseRelationDAL,
                CoureChangeRelationDAL]
        for dal in dals:
            dal.instance_list = []

        cs = MajorDAL.new(name='计算机系',
                          total_score=12,
                          required_scores=[2, 2, 2, 2, 2, 2])
        math = MajorDAL.new(name='数学系',
                            total_score=12,
                            required_scores=[2, 2, 2, 2, 2, 2])

        s0 = StudentDAL.new(name='A',
                            sex='male',
                            major_id=cs.id)
        s1 = StudentDAL.new(name='B',
                            sex='female',
                            major_id=math.id)

        gaoshu = CourseDAL.new(name='高等数学',
                               score=2,
                               teacher_name='teacher gao')
        lisanshuxue = CourseDAL.new(name='离散数学',
                                    score=2,
                                    teacher_name='teacher li')

        # 一个计算机的学生和一个数学系的学生
        # 高数对计算机的来说是基础必修课，离散对计算机的来说是专业必修课
        # 高数对数学系的来说是专业必修课
        major_coure_relation0 = MajorCourseRelationDAL.new(major_id=cs.id,
                                                           course_id=gaoshu.id,
                                                           type=CourseType.universal_required_basic.value)
        major_coure_relation1 = MajorCourseRelationDAL.new(major_id=cs.id,
                                                           course_id=lisanshuxue.id,
                                                           type=CourseType.professional_required_basic.value)
        major_coure_relation2 = MajorCourseRelationDAL.new(major_id=math.id,
                                                           course_id=gaoshu.id,
                                                           type=CourseType.professional_required_basic.value)

        student_course_relation0 = StudentCourseRelationDAL.new(student_id=s0.id,
                                                                course_id=gaoshu.id,
                                                                time='2021春季学期',
                                                                type=CourseType.universal_required_basic.value)
        student_course_relation1 = StudentCourseRelationDAL.new(student_id=s1.id,
                                                                course_id=gaoshu.id,
                                                                time='2021春季学期',
                                                                type=CourseType.professional_required_basic.value)

        course_change_relation0 = CoureChangeRelationDAL.new(source_course_id=lisanshuxue.id,
                                                             dest_coure_id=gaoshu.id)

    def help(self):
        return '重新初始化所有数据，指令格式：i'
