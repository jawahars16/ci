import importlib
import inspect
import logging
import os
import re

from task.impl.task import Task
from task.impl.task_base import TaskBase


class TaskLoader:

    def __init__(self, path):
        self.path = path


    def __resolve_category__(self, category, delimiter):
        if category is None:
            return ''
        else:
            return f'{delimiter}{category}'


    def load_tasks(self, category = None):
        '''
        Load all the plugins in given directory
        :param category: sub directory
        :return: list of Task objects
        '''
        search_path = f'{self.path}{self.__resolve_category__(category, "/")}'
        logging.debug(f'Searching tasks in {search_path}')
        pysearchre = re.compile('.py$', re.IGNORECASE)
        pluginfiles = filter(pysearchre.search,
                             os.listdir(search_path))

        form_module = lambda fp: '.' + os.path.splitext(fp)[0]
        plugins = map(form_module, pluginfiles)

        module_name = f'task{self.__resolve_category__(category, ".")}'
        logging.debug(f'Importing module {module_name}')

        # TODO: Check importing parent module / namespace really required?
        # importlib.import_module(module_name)

        tasks = []
        for plugin in plugins:
            if not plugin.startswith('.__'):
                logging.debug(f'Importing plugin {plugin}')
                clazz = self.load_task(module_name, plugin)
                task = Task(f'{plugin}@{module_name}', re.sub(r"(\w)([A-Z])", r"\1 \2", clazz.__name__), clazz().__doc__)
                tasks.append(task)

        return tasks


    def load_task(self, module_name, plugin):
        module = importlib.import_module(plugin, package=module_name)
        clazzes = inspect.getmembers(module, lambda clz:
        inspect.isclass(clz) and
        issubclass(clz, TaskBase) and
        not inspect.isabstract(clz))
        if clazzes is None or len(clazzes) < 1:
            raise NotImplementedError("No class found to implement the abstract class 'TaskBase'")
        if len(clazzes) > 1:
            raise RuntimeError("More than one class found to implement the abstract class 'TaskBase'")
        className = clazzes[0][0]
        clazz = getattr(module, className)
        return clazz


mod = importlib.import_module('.test_task', 'task.test')
print(mod)