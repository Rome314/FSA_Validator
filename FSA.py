class State:


    def __init__(self, state: str):
        self.state = state
        self.vis = False
        self.inputs = list()
        self.outputs = list()
        self.commands = dict()




class Transition:


    def __init__(self, trans):
        self.trans = trans
        self.from_state = None
        self.to_state = None


class FSA:

    def __init__(self):
        self.transitions = dict()
        self.states = dict()
        self.initial = None
        self.final = list()
        self.warnings = list()

    def add_state(self, state):
        self.states[state] = State(state)

    def add_transition(self, trans: Transition):
        self.transitions[trans] = Transition(trans)

    def get_state(self, state):
        if state in self.states:
            return self.states[state]
        else:
            return -1

    def get_transition(self, transition):
        if transition in self.transitions:
            return self.transitions[transition]
        else:
            return -1


    def get_info(self):
        print(self.states)
        print(self.transitions)
        print(self.initial)
        print(self.final)
        print()
        print(self.warnings)
