from concurrent.futures import Executor, ThreadPoolExecutor
from typing import NoReturn

from config.models import AggregatedResource
from listeners.resource_listener import MultiResourceListener, ResourceListener


class ThreadedMultiResourceListener(MultiResourceListener):
    def __init__(self, resource_listener: ResourceListener):
        self._resource_listener: ResourceListener = resource_listener
        self._pool_executor: type[Executor] = ThreadPoolExecutor

    def listen(self, aggregated_resources: list[AggregatedResource]) -> NoReturn:
        with self._pool_executor(max_workers=len(aggregated_resources)) as executor:
            for aggregated_resource in aggregated_resources:
                executor.submit(self._resource_listener.listen, aggregated_resource)
