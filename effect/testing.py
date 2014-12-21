"""
Various functions for inspecting and restructuring effects.
"""

from __future__ import print_function


class CannedDispatcher(object):

    def __init__(self):
        self._expected = []

    def add_success(self, intent, result):
        self._expected.append((intent, False, result))

    def add_failure(self, intent, result):
        self._expected.append((intent, True, result))

    def __call__(self, dispatcher, intent, box):
        expected, is_error, result = self._expected.pop(0)
        if intent == expected:
            if is_error:
                box.fail(result)
            else:
                box.succeed(result)
        else:
            raise AssertionError("Unexecpected intent.")
