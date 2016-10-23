"""
Controller
==========

This module implements the elevator controller mechanism. It is responsible for
tracking, dispatching, and idling elevators.
"""


from building import Building, Person
from elevator import Elevator
from datastructures import Queue


UP = 1
DOWN = -1


class Controller(object):
    """ The main controller """

    def __init__(self, number_of_floors=None, number_of_elevators=None):
        self.building = Building(number_of_floors, number_of_elevators)
        self.request_queue = Queue()
        self.up_queue = Queue()
        self.down_queue = Queue()

    def call_elevator(self, direction, curr_floor, dest_floor):
        """
        Calls the elevator to the requested floor.

        :param direction:
            Direction chosen when requesting elevator (1 is up, -1 is down)
        :type direction: 1 or -1
        :param current_floor: Floor that the elevator was requested
        :type current_floor: int
        :param destination_floor: The floor chosen after arrival to floor
        :type destination_floor: int
        """

        self.request_queue.push(Person(direction, curr_floor, dest_floor))

    def run_until_stop(self):
        """ Runs the elevator system until an elevator stops """

        steps = 1
        self._run(steps, True, False)

    def run(self, steps=None):
        """
        Runs the elevator system for the specified number of steps. Defaults
        to one step if steps isn't specified. Halts when all elevators have
        stopped.
        """

        if steps is None:
            steps = 1
        self._run(steps, False, True)

    def _run(self, steps=None, first_to_stop=False, all_to_stop=False):
        """
        Runs the elevator system for the specified number of steps.

        :param steps: Number of steps to run through (defaults to 1)
        :type steps: int
        :param first_to_stop: Should the system halt when an elevator stops
        :type first_to_stop: bool
        :param all_to_stop: Should the system half when all elevators stop
        :type all_to_stop: bool
        """

        if steps is None or (first_to_stop == all_to_stop):
            raise ValueError(
                "Not only must steps must be an integer greater than zero,"
                "but also first_to_stop and all_to_stop cannot be equal"
            )

        for request in self.request_queue:
            if request.direction == UP:
                self.up_queue.push(request)
            elif request.direction == DOWN:
                self.down_queue.push(request)
            else:
                raise ValueError(
                    "Up value must be 1, and down value must be -1."
                    " Got: " + str(request.direction)
                )
