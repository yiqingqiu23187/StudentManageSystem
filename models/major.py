from models.base_model import BaseModel

class Major(BaseModel):
    def __init__(self, id=None, name=None, total_score=None, required_scores=None):
        super(Major, self).__init__(id)
        self.name = name
        self.total_score = total_score
        self.required_scores = required_scores