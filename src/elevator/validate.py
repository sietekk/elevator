"""
Input Validation
================

This module contains the classes necessary for user input validation. The
instantiated classes all receive input from :func:`raw_input`, validate it,
and return the data type specified in the validator class definition. Based on
the implementation from :mod:`rex.core.validate` version 1.11.2.

Implementations must subclass :class:`Validate`.
"""


import six


from error import Error, guard


class Validate(object):

    def __call__(self, data):
        """
        Applies the validator to the input value.

        Subclasses must override this method.
        """

        raise NotImplementedError("%s.__call__()" % self.__class__.__name__)


class StrVal(Validate):
    """
    Accepts :mod:`six.string_types` string values.

    If `pattern` is given, the whole input must match the regex pattern.
    """

    pattern = None

    def __init__(self, pattern=None):
        # Allow to specify the pattern in a subclass.
        self.pattern = pattern or self.__class__.pattern

    def __call__(self, data):
        with guard("Got:", repr(data)):
            if not isinstance(data, six.string_types):
                raise Error("Expected a string")
            if self.pattern is not None and \
                    re.match(r"\A(?:{})\Z".format(self.pattern), data) is None:
                raise Error(
                    "Expected a string matching:", "/{}/".format(self.pattern)
                )
        return data


class ChoiceVal(Validate):
    """
    Accepts and validates strings from a fixed set of choices.

    Expects a list of strings::

        >>> choice = ChoiceVal(['1', '2', 'waffles', ])
        >>> choice('2')
        '2'
        >>> choice('foobar')
        ...
        elevator.error.Error: Expected one of:
            1, 2, waffles
        Got:
            'foobar'

    """

    def __init__(self, *choices):
        if len(choices) == 1 and isinstance(choices[0], list):
            [choices] = choices
        self.choices = choices

    def __call__(self, data):
        with guard("Got:", repr(data)):
            if not isinstance(data, six.string_types):
                raise Error("Expected a string")
            if data not in self.choices:
                raise Error("Expected one of:", ", ".join(self.choices))
        return data
