from models.base_model import BaseModel

class Course(BaseModel):
    def __init__(self, id=None, name=None, score=None, teacher_name=None):
        super().__init__(id)
        self.score = score
        self.teacher_name = teacher_name
        self.name = name
