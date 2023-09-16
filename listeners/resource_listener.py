import abc
from typing import NoReturn

from config.models import AggregatedResource


class ResourceListener(abc.ABC):
    @abc.abstractmethod
    def listen(self, aggregated_resource: AggregatedResource) -> NoReturn:
        raise NotImplementedError


class MultiResourceListener(abc.ABC):
    @abc.abstractmethod
    def listen(self, aggregated_resources: list[AggregatedResource]) -> NoReturn:
        raise NotImplementedError
