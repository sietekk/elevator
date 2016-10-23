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

    def __init__(self, label, init_floor):
        self.label = label
        self.floor = init_floor
        self.machine = Machine(
            model=self,
            states=Elevator.states,
            transitions=Elevator.transitions,
            initial='idle'
        )

    @classmethod
    def create_elevator(cls, label, init_floor):
        return cls(label, init_floor)
