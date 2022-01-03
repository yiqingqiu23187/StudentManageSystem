import importlib
import inspect
import pkgutil
import services as target_services
from services.base_service import BaseService
from common.singleton import singleton_wrapper

@singleton_wrapper
class Router(object):

    def __init__(self):
        self.CODE_SERVICE_MAP = {}

    def _get_module_list(self, services_package):
        modules = []
        for file_finer, name, is_pkg in pkgutil.iter_modules(services_package.__path__,
                                                             services_package.__name__ + "."):
            if not is_pkg:
                modules.append(importlib.import_module(name))
            else:
                md = importlib.import_module(name)
                modules = modules + self._get_module_list(md)
        return modules

    def _service_register(self):
        class_list = []
        class_tuple_list = []
        modules = self._get_module_list(target_services)
        for md in modules:
            class_members = inspect.getmembers(md, inspect.isclass)
            class_tuple_list = class_tuple_list + class_members

        # 获取所有类列表
        class_tuple_list = list(set(class_tuple_list))
        for clazz_name, clazz in class_tuple_list:
            if issubclass(clazz, BaseService) and not issubclass(BaseService, clazz):
                class_list.append(clazz)

        for clazz in class_list:
            self.CODE_SERVICE_MAP.update({clazz().get_code(): clazz})

    def find_route(self, code):
        # type: (str) -> BaseService
        if not len(self.CODE_SERVICE_MAP):
            self._service_register()
        if code in self.CODE_SERVICE_MAP:
            return self.CODE_SERVICE_MAP[code]
        else:
            raise Exception('不存在的指令')


