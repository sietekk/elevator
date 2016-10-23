#
# Copyright (c) 2016 Michael Conroy
#


from collections import OrderedDict, namedtuple
from elevator import Elevator


DEFAULT_FLOOR_QTY = 50
DEFAULT_ELEVATOR_QTY = 4


class Building(object):
    """ Container object for elevators """

    def __init__(self, number_of_floors=None, number_of_elevators=None):
        self.floors = []
        self.elevators = []

        # Generate floors
        if number_of_floors is None:
            floor_count = DEFAULT_FLOOR_QTY
        else:
            floor_count = number_of_floors

        for number in xrange(1, floor_count+1):
            self.floors.append(Floor(number))

        # Generate elevators
        if number_of_elevators is None:
            elevator_count = DEFAULT_ELEVATOR_QTY
        else:
            elevator_count = number_of_elevators

        for identifier in xrange(1, elevator_count+1):
            # TODO: Stagger initialized floors across entire building
            self.elevators.append(Elevator(identifier, 0))

    def __iter__(self):
        for elevator in self.elevators:
            yield elevator


# TODO: Determine if we indeed need a floor object
class Floor(namedtuple('Floor', 'number')):

    __slots__ = ()


class Person(namedtuple('Person', 'direction curr_floor dest_floor')):
    """
    Represents a person (rider).

    A person chooses a direction when requesting an elevator from the
    current floor, and then after entering the elevator, requests the
    destination floor.
    """

    __slots__ = ()
