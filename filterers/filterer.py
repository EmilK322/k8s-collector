import abc

from config.models import Resource


class EventFilterer(abc.ABC):
    @abc.abstractmethod
    def filter(self, event: dict, resource: Resource) -> dict | None:
        raise NotImplementedError


