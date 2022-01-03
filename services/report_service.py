import openpyxl
from services.base_service import BaseService
from dals.student_dal import StudentDAL
from dals.major_dal import MajorDAL
from dals.course_dal import CourseDAL
from dals.major_coure_relation_dal import MajorCourseRelationDAL
from dals.student_course_relation_dal import StudentCourseRelationDAL
from common.constants import CourseType


class ReportService(BaseService):
    def get_code(self):
        return 'r'

    def help(self):
        return '生成进度报告，指令格式：r 学生id或姓名 专业方向'

    def process(self, data):  # type: (str) -> None
        _, student_id, direction = data.split()
        # 计算数据
        student = StudentDAL.query_by_id_or_name(student_id)
        if not student:
            raise Exception('学生不存在')
        major = MajorDAL.query_by_id(student.major_id)
        courses = [[] for _ in range(5)]
        for instance in StudentCourseRelationDAL.instance_list:
            if instance.student_id == student.id:
                course = CourseDAL.query_by_id(instance.course_id)
                if instance.source_course_id:
                    source_course = CourseDAL.query_by_id(instance.source_course_id)
                    comment = '该课程由' + str(source_course.id) + '-' + str(source_course.name) + '转化而来'
                else:
                    comment = ''
                courses[instance.type].append([str(course.id) + '-' + str(course.name), course.score, comment])

        # 写入表格
        wb = openpyxl.Workbook()
        ws = wb.active
        # 进度汇总
        ws.append(['学号', '姓名', '专业', '方向'])
        ws.append([student.id, student.name, major.name, direction])
        ws.append(['进度汇总'])
        ws.append(['专业+方向'])
        ws.append(['课程类型', '已修学分', '已修课程数量', '要求学分/课程数量', '进度情况'])
        actual_score = sum(x[1] for x in courses[CourseType.universal_required_basic.value]) + sum(
            x[1] for x in courses[CourseType.professional_required_basic.value])
        required_score = major.required_scores[CourseType.universal_required_basic.value] + major.required_scores[
            CourseType.professional_required_basic.value]
        ws.append(['必修的基础课与专业基础课',
                   actual_score,
                   len(courses[CourseType.universal_required_basic.value]) + len(
                       courses[CourseType.professional_required_basic.value]),
                   required_score,
                   "%.2f%%" % max(1, actual_score / required_score)
                   ])
        for course_type in range(CourseType.professional_optional_nondirection.value, CourseType.any.value):
            actual_score = sum(x[1] for x in courses[course_type])
            required_score = major.required_scores[course_type]
            ws.append(['专业选修课',
                       actual_score,
                       len(courses[course_type]),
                       required_score,
                       "%.2f%%" % max(1, actual_score / required_score)
                       ])

        # 进度详情
        ws.append(['进度详情'])
        ws.append(['必修的基础课与专业基础课'])
        ws.append(['课程', '学分', '备注'])
        actual_score = sum(x[1] for x in courses[CourseType.universal_required_basic.value]) + sum(
            x[1] for x in courses[CourseType.professional_required_basic.value])
        required_score = major.required_scores[CourseType.universal_required_basic.value] + major.required_scores[
            CourseType.professional_required_basic.value]
        for course in courses[CourseType.universal_required_basic.value]:
            ws.append(course)
        for course in courses[CourseType.professional_required_basic.value]:
            ws.append(course)
        ws.append(['总结', '要求 %s 学分，缺少 %s 学分' % (required_score, required_score - actual_score),
                   "%.2f%%" % max(1, actual_score / required_score)])

        titles = ['基础课', '专业基础课', '专业选修课', '模块课', '方向课', '任意选修课']
        for course_type in range(CourseType.professional_optional_nondirection.value, CourseType.any.value):
            ws.append([titles[course_type]])
            ws.append(['课程', '学分', '备注'])
            actual_score = sum(x[1] for x in courses[course_type])
            required_score = major.required_scores[course_type]
            for course in courses[course_type]:
                ws.append(course)
            ws.append(['总结', '要求 %s 学分，缺少 %s 学分' % (required_score, required_score - actual_score),
                       "%.2f%%" % max(1, actual_score / required_score)])

        wb.save('reports/test.xlsx')
