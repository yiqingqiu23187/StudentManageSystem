from services.base_service import BaseService

class AddService(BaseService):
    def get_code(self):
        return 'a'

    def process(self, data):  # type: (str) -> None
        # TODO: 可以自主增加学生、专业和课程，暂时采用系统固定初始化
        pass
