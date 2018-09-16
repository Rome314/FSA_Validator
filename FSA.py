class State:
    inputs = []
    outputs = []

    def __init__(self, state: str):
        self.__state = state
        self.__vis = False

    def get_state(self):
        return self.__state
    def get_vis(self):
        return self.__vis



class Transition:
    from_state = None
    to_state = None

    def __init__(self, trans: list):
        self.trans = trans


class FSA:
    def __init__(self):
        self.transitions = dict()
        self.states = dict()
        self.initial = None
        self.final = list()

    def add_state(self, state: State):
        self.transitions[state.get_state()] = state

    def add_transition(self, trans: Transition):
        self.transitions[trans.alpha] = trans

    def get_state(self,state):
        if state.get_state() in self.states:
            return self.states[state.get_state()]
        else:
            return -1

    def get_transition(self, transition):
        if transition in self.transitions[transition.trans]:
            return self.transitions[transition.trans]
        else:
            return -1



