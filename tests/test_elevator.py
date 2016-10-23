#
# Copyright (c) 2016 Michael Conroy
#


from elevator.elevator import Elevator


def test_elevator():
    try:
        e1 = Elevator()
    except Exception as exc:
        if isinstance(exc, TypeError):
            pass
        else:
            raise exc

    e2 = Elevator(1, 100)
    assert e2.identifier == 1, "Identifier initializes to incorrect value"
    assert e2.floor == 100, "Floor initializes to incorrect value"

    e3 = Elevator.create_elevator(4, 15)
    assert e3.identifier == 4, "Identifier initializes to incorrect value"
    assert e3.floor == 15, "Floor initializes to incorrect value"
