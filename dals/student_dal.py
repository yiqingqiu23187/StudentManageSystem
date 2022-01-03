from models.student import Student
from dals.base_dal import BaseDAL

class StudentDAL(BaseDAL):
    model_class = Student
    instance_list = []
