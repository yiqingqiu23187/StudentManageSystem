from typing import List, Any

from dals.base_dal import BaseDAL
from models.course_change_relation import CoureChangeRelation

class CoureChangeRelationDAL(BaseDAL):
    model_class = CoureChangeRelation
    instance_list: list[CoureChangeRelation] = []
