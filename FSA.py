#File with classes for

class State:

    def __init__(self, state: str): #Initialization for states
        self.state = state #Name
        self.inputs = list() #Which from  states can be arrived
        self.outputs = list() # Where to states can go
        self.commands = dict() #Which transitions can be used and where to it will go


class Transition:

    def __init__(self, trans):
        self.trans = trans #Name
        self.from_state = None #What from
        self.to_state = None #where to


class FSA: #MAchine class

    def __init__(self):
        self.transitions = dict() #Possible transitions (Alpha)
        self.states = dict() #Possible states
        self.initial = None
        self.final = list()
        self.warnings = list() #List with handled warnings

    def add_state(self, state):
        self.states[state] = State(state)

    def add_transition(self, trans: Transition):
        self.transitions[trans] = Transition(trans)

    def get_state(self, state):
        if state in self.states.keys():
            return self.states.get(state)
        else:
            return -1

    def get_transition(self, transition):
        if transition in self.transitions:
            return self.transitions[transition]
        else:
            return -1

    def get_info(self): #Printing main info
        print(self.states)
        print(self.transitions)
        print(self.initial)
        print(self.final)
        print()
        print(self.warnings)
