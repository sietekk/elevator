#
# Copyright (c) 2016 Michael Conroy
#


from transitions import Machine


class Elevator(object):

    states = [
        'up',
        'down',
        'arrived',
        'idle',
    ]

    transitions = [
        {
            'trigger': 'arrive',
            'source': ['up', 'down', ],
            'dest': 'arrived'
        },
        {
            'trigger': 'start',
            'source': 'idle',
            'dest': ['up', 'down', ],
        },
        {
            'trigger': 'stop',
            'source': 'arrived',
            'dest': 'idle'
        },
        {
            'trigger': 'move',
            'source': 'arrived',
            'dest': ['up', 'down', ],
        },
    ]

    def __init__(self, identifier, init_floor):
        self.identifier = identifier
        self.floor = init_floor
        self.machine = Machine(
            model=self,
            states=Elevator.states,
            transitions=Elevator.transitions,
            initial='idle'
        )

    @classmethod
    def create_elevator(cls, identifier, init_floor):
        return cls(identifier, init_floor)
