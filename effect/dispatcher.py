"""
Dispatcher!
"""

from itertools import ifilter
from characteristic import attributes


@attributes(['mapping'], apply_with_init=False)
class TypeDispatcher(object):
    """
    An Effect dispatcher which looks up the performer to use by type.
    """
    def __init__(self, mapping):
        """
        :param collections.Mapping mapping: A mapping of intent type to
        performer.
        """
        self.mapping = mapping

    def __call__(self, intent):
        return self.mapping.get(type(intent))


@attributes(['dispatchers'], apply_with_init=False)
class ComposedDispatcher(object):
    """
    A dispatcher which composes other dispatchers.

    The dispatchers given will be searched in order until a performer is found.
    """
    def __init__(self, dispatchers):
        """
        :param collections.Iterable dispatchers: Dispatchers to search.
        """
        self.dispatchers = dispatchers

    def __call__(self, intent):
        return next(ifilter(None, (d(intent) for d in self.dispatchers)), None)
