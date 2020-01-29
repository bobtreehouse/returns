# -*- coding: utf-8 -*-

from typing import Any, NoReturn

from returns.primitives.exceptions import ImmutableStateError


class Immutable(object):
    """
    Helper type for objects that should be immutable.

    When applied, each instance becames immutable.
    Nothing can be added or deleted from it.

    .. code:: python

      >>> from returns.primitives.types import Immutable
      >>> class MyModel(Immutable):
      ...     ...
      ...
      >>> model = MyModel()

    .. code::

      >>> model.prop = 1
      Traceback (most recent call last):
         ...
      returns.primitives.exceptions.ImmutableStateError

    See :class:`returns.primitives.container.BaseContainer` for examples.

    """

    def __setattr__(self, attr_name: str, attr_value: Any) -> NoReturn:
        """Makes inner state of the containers immutable for modification."""
        raise ImmutableStateError()

    def __delattr__(self, attr_name: str) -> NoReturn:  # noqa: WPS603
        """Makes inner state of the containers immutable for deletion."""
        raise ImmutableStateError()
