from services.init_service import InitService
from common.helper.executor import Executor

if __name__ == '__main__':
    InitService().process('i')
    executor = Executor()
    while True:
        executor.execute(input())