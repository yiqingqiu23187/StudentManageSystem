from models.major import Major
from dals.base_dal import BaseDAL


class MajorDAL(BaseDAL):
    model_class = Major
    instance_list = []

