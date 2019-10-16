import sys
import re

def parseSS(str):
    return re.search("[0-9]+", re.search("ss\([0-9]+,", str).group(0)).group(0)
        
def parseTransition(str):
    transitions = []
    transition_group = re.findall("\[[0-9]+\|[0-9]+\]", str)
    for transition in transition_group:
        ts = re.findall("[0-9]+", transition)
        transitions.append([ts[0], ts[1]])
    return transitions

def parseState(str):
    states = {}
    state_group = re.findall("state\([0-9]+,\{.*?\}\)", str)
    for state in state_group:
        id = re.search("[0-9]+", state).group(0)
        name = re.search("\{.*?\}", state).group(0)
        states[id] = name
    return states


def toDot(str):
    ss_id = parseSS(str)
    transitions = parseTransition(str)
    states = parseState(str)
    print("digraph states {")
    for transition in transitions:
        print('"', states[transition[0]], '"', "->", '"', states[transition[1]], '"', ";")
    print("}")

if __name__ == "__main__":
    str = ""
    if len(sys.argv) == 1:
        str = input()
    elif len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            str = f.read()
    else:
        print('Usage: "python3 lmnToDot.py [filename]"')
        sys.exit()
    toDot(str)
