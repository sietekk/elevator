#
# Copyright (c) 2016 Michael Conroy
#


from elevator.building import (
    Building,
    Floor,
    DEFAULT_FLOOR_QTY,
    DEFAULT_ELEVATOR_QTY,
)
from elevator.elevator import Elevator


def test_building():
    b1 = Building()
    assert len(b1.floors) == DEFAULT_FLOOR_QTY, \
        "Incorrect default number of floors"

    assert len(b1.elevators) == DEFAULT_ELEVATOR_QTY, \
        "Incorrect default number of elevators"

    b2 = Building(20, 5)
    assert len(b2.floors) == 20, \
        "Initialize to wrong number of floors"

    assert len(b2.elevators) == 5, \
        "Initialized to wrong number of elevators"

    for elevator in b2:
        assert isinstance(elevator, Elevator), \
            "Elevator object not instantiated with Elevator class"

    for floor in b2.floors:
        assert isinstance(floor, Floor), \
            "Floor object not instantiated with Floor class"
