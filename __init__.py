import FSA
import parser
from string_stuff import *


def main():
    inp = "fsa.txt"
    out = "result.txt"
    output = open(out, "w")
    data = parser.parse_input(inp, out)
    machine = FSA.FSA()

    for state in data[0]:
        machine.add_state(state)

    for transition in data[1]:
        machine.add_transition(transition)

    if machine.get_state(data[2]) == -1:
        error = E1
        output.write("Error:\n" + error)
        output.close()
        exit(0)
    else:
        machine.initial = machine.get_state(data[2])

    if len(data[3]) == 0:
        machine.warnings.append(W1)
    else:
        for fin_state in data[3]:
            state = machine.get_state(fin_state)
            if state == -1:
                error = E1
                output.write("Error:\n" + error)
                output.close()
                exit(0)
            else:
                machine.final.append(state)

    for path in data[4]:
        elements = path.split(">")
        if ((machine.get_state(elements[0]) == -1) or (machine.get_state(elements[2]) == -1)):
            error = E1
            output.write("Error:\n" + error)
            output.close()
            exit(0)
        else:
            state_left = machine.get_state(elements[0])
            state_right = machine.get_state(elements[2])
            if (machine.get_transition(elements[1]) == -1):
                error = "A transition '" + elements[1] + "' is not represented in the alphabet"
                output.write("Error:\n" + error)
                output.close()
                exit(0)
            else:
                trans = machine.get_transition(elements[1])
                trans.from_state = state_left
                trans.to_state = state_right
                state_left.commands[elements[1]] = state_right
                if (state_right.state != state_left.state):
                    state_left.outputs.append(state_right)
                    state_right.inputs.append(state_left)
                    state_left.outputs = list(set(state_left.outputs))
                    state_right.inputs = list(set(state_right.inputs))

    for state in machine.states.values():
        if len(state.inputs) == 0:
            error = E2
            output.write("Error:\n" + error)
            output.close()
            exit(0)


if __name__ == "__main__":
    main()

# print()
# print()
# print()
# machine.get_info()
# print()
# print()
# print()
# print(machine.get_state("on").outputs[0].state)
