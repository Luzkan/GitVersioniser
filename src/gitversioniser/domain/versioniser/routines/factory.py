from abc import ABC, abstractmethod


class RoutineFactory(ABC):
    @staticmethod
    def skip_init(external_class):
        original_init = external_class.__init__
        external_class.__init__ = lambda *args, **kwargs: None
        class_instance = external_class()
        external_class.__init__ = original_init
        return class_instance

    @staticmethod
    @abstractmethod
    def create(routine_name: str):
        pass
