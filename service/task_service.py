import importlib
import os
import logging
import sys
from pkgutil import iter_modules

from common.constants import Constants
from model.task import Task
from task.task_base import TaskBase


class TaskService:

    def get_all_tasks(self):
        path = os.path.join(os.path.dirname(__file__).replace('service',''), "task\\util")
        logging.debug(f'Looking for tasks in {path}')

        modules = iter_modules(path=[path])

        for mod in modules:
            logging.debug(mod)
            # sys.path.append(f'{path}\\{mod.name}')
            # module = importlib.import_module(f'{path}\\{mod.name}')
            # logging.debug(module)
    #
    #
    # def load_task(self, mod_name):
    #     logging.debug(mod_name)
    #     if mod_name not in sys.modules:
    #         # Import module
    #         loaded_mod = __import__(f'{self.path}\\{mod_name}', fromlist=[mod_name])
    #         logging.debug(loaded_mod)
