"""
User Input Parsing
==================

This module contains the classes and function necessary to handle user input
and validation of user input.
"""


import six


from error import Error


def prompt(prompt=None, validator=None, tries=None):
    """
    User input parser.

    :param prompt: Prompt text to direct user input
    :type prompt: str
    :param validator: Validator to apply to user input
    :type validator: class instance
    :param tries: Number of tries before quitting
    :type tries: int
    :returns: User input converted to validator data type
    :rtype: Any built-in type
    """

    if prompt is None or not isinstance(prompt, six.string_types):
        raise Error("Prompt must be a valid string")

    if validator is None or not issubclass(validator.__class__, Validate):
        raise Error("Expected a validator instance")

    # Loop until valid input given
    count = 1
    while True:
        try:
            input = raw_input(prompt)
            return validator(input)
        except Error as err:
            log(msg=str(err))
            if tries is not None:
                if tries == count:
                    raise Error("Max tries reached, exiting application")
                else:
                    count += 1
