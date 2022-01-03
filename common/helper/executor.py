from common.exception import exception_wrapper
from common.helper.router import Router


class Executor(object):
    def __init__(self):
        self.router = Router()

    # @exception_wrapper()
    def execute(self, string):
        # type: (str) -> None
        params = string.split()
        target_service = self.router.find_route(params[0])()
        target_service.process(string)
