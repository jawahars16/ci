from task import input
from task.input import Input
from task.task_base import TaskBase


class DeleteFiles(TaskBase):

    def get_inputs(self):
        target_directory = Input('target', 'Target Directory', 'text', '', True)
        include_sub_directories = Input('include_sub', 'Include Sub directories', 'checkbox', )

    def run(self):
        pass
