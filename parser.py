from string_stuff import *


def parse_input(inp: str, out: str):
    inp_file = open(inp,"r")
    out_file = open(out,"w")
    line = inp_file.readline()
    line.strip().replace(" ", "")
    if line.startswith("states={"):
        states_line = line[8:-2]
        states = states_line.split(",")
    else:
        error = E5
        out_file.write("Error:\n" + error)
        out_file.close()
        exit(0)

    line = inp_file.readline()
    line.strip().replace(" ", "")
    if line.startswith("alpha={"):
        alpha_line = line[7:-2]
        alpha = alpha_line.split(",")
    else:
        error = E5
        out_file.write("Error:\n" + error)
        out_file.close()
        exit(0)

    line = inp_file.readline()
    line.strip().replace(" ", "")
    if line.startswith("init.st={"):
        init_state = line[9:-2]

        if len(init_state) == 0:
            error = E4
            out_file.write("Error:\n" + error)
            out_file.close()
            exit(0)

    else:
        error = E5
        out_file.write("Error:\n" + error)
        out_file.close()
        exit(0)

    line = inp_file.readline()
    line.strip().replace(" ", "")
    if line.startswith("fin.st={"):
        fin_line = line[8:-2]
        if len(fin_line) != 0:
            finite_states = fin_line.split(",")
        else:
            finite_states = []
    else:
        error = E5
        out_file.write("Error:\n" + error)
        out_file.close()
        exit(0)

    line = inp_file.readline()
    line.strip().replace(" ", "")
    if line.startswith("trans={"):
        trans_line = line[7:-1]
        trans = trans_line.split(",")
    else:
        error = E5
        out_file.write("Error:\n" + error)
        out_file.close()
        exit(0)

    return [states,alpha,init_state,finite_states,trans]
