from common.helper.router import Router
from services.base_service import BaseService


class HelpService(BaseService):
    def get_code(self):
        return 'h'

    def process(self, data):  # type: (str) -> None
        for service_class in Router().CODE_SERVICE_MAP.values():
            help_info = service_class().help()
            if help_info:
                print(help_info)

    def help(self):
        return '获取所有指令使用方式，指令格式：h'