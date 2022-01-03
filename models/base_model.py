class BaseModel(object):
    unique_id = 0
    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            BaseModel.unique_id += 1
            self.id = BaseModel.unique_id
