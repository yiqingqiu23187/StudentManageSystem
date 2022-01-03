from models.base_model import BaseModel


class BaseDAL(object):
    model_class = BaseModel

    instance_list = []

    @classmethod
    def new(cls, **fields):
        result = cls.model_class() # type: cls.model_class
        for key, val in fields.items():
            if hasattr(result, key):
                setattr(result, key, val)
        cls.instance_list.append(result)
        return result

    @classmethod
    def query_by_id(cls, id):
        for instance in cls.instance_list:
            if instance.id == id:
                return instance
        return None

    @classmethod
    def query_by_id_or_name(cls, id_or_name):
        # 先查id后查name
        for instance in cls.instance_list:
            if instance.id == id_or_name:
                return instance
            if instance.name == id_or_name:
                return instance
        return None
