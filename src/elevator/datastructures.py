#
# Copyright (c) 2016 Michael Conroy
#


class Queue(object):
    """
    Implementation of a basic FIFO queue ADT using the standard lib's
    collection's deque ADT (fast atomic append() and popleft() operations that
    do not require locking unlike the standard lib's Queue package).

    https://docs.python.org/2/library/queue.html
    """

    def __init__(self):
        self._internal = collections.deque()

    def push(self, new):
        # Only append to right side
        self._internal.append(new)

    def pop(self):
        # Only pop from the left side
        self._internal.popleft()

    def peek(self):
        return self._internal[0]

    def size(self):
        return len(self._internal)

    def is_empty(self):
        return len(self._internal) == 0

    def __iter__(self):
        # DANGER: Iteration empties the queue!
        while not self.is_empty():
            item = self.pop()
            yield item
