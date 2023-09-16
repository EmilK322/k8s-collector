from jmespath.parser import ParsedResult

from config.models import Resource
from filterers.filterer import EventFilterer
from utils.jmespath import JmesPathQueryCache


class JmesPathEventFilterer(EventFilterer):
    def __init__(self):
        self._resources_to_query_cache: JmesPathQueryCache = JmesPathQueryCache()

    def filter(self, event: dict, resource: Resource) -> dict | None:
        raw_object: dict = event['raw_object']
        compiled_query: ParsedResult = self._resources_to_query_cache.get_or_set(resource.selector.query)
        selector_query_matched: bool = compiled_query.search(raw_object)
        return event if selector_query_matched else None
