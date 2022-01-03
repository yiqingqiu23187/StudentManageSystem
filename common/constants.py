from enum import Enum

class CourseType(Enum):
    universal_required_basic = 0                # 基础必修课
    professional_required_basic = 1             # 专业必修课
    professional_optional_nondirection = 2      # 专业选修课
    universal_optional_model = 3                # 模块课
    professional_optional_direction = 4         # 方向课
    any = 5                                     # 任意选修课
