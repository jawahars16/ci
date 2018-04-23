from abc import ABC, abstractmethod


class TaskBase(ABC):

    @abstractmethod
    def get_inputs(self):
        pass

    def validate_inputs(self):
        pass

    @abstractmethod
    def run(self):
        pass

    def on_remove(self):
        pass