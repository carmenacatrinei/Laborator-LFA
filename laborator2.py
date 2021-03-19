import argparse

def argumente_terminal():
    parser = argparse.ArgumentParser()
    parser.add_argument('fisier')
    parser.add_argument('cuvant')
    args = parser.parse_args()

    return args.fisier, args.cuvant

def citire_fisier(fisier):
    f = open(fisier, "r")
    line = f.readline()
    sigma = []
    states = []
    transitions = []
    while line:
        if line.startswith('Sigma'):
            line = f.readline()
            while line.startswith('End') is False:
                line = line.replace(" ", "").strip('\t\n')
                sigma.append(line)
                line = f.readline()
        elif line.startswith('States'):
            line = f.readline()
            while line.startswith('End') is False:
                line = line.replace(" ", "").strip('\t\n')
                line = line.split(',')
                states.append(line)
                line = f.readline()
        elif line.startswith('Transitions'):
            line = f.readline()
            while line.startswith('End') is False:
                line = line.replace(" ", "").strip('\t\n')
                line = line.split(',')
                transitions.append(line)
                line = f.readline()
        line = f.readline()

    return sigma, states, transitions

def verificare_fisier(sigma, states, transitions):
    erori = 0
    for transition in transitions:
        if transition[1] not in sigma:
            erori += 1
        nod1 = nod2 = 0
        for state in states:
            if state[0] == transition[0]:
                nod1 = 1
            if state[0] == transition[2]:
                nod2 = 1
        if nod1 == 0:
            erori += 1
        if nod2 == 0:
            erori += 1
    numar = 0
    for i in range(len(states)):
        if len(states[i]) > 1 and states[i][1] == "S":
            numar += 1
            stare_initiala = states[i][0]
    if erori != 0:
        print("Exista " + str(erori) + " date gresite!")
        stare_initiala = -1
    if numar != 1:
        print("Atentie! Aveti: " + str(numar) + " stari initiale")
        stare_initiala = -1

    return stare_initiala

def verificare_dfa(cuvant, stare_initiala, states, transitions):
    stare_curenta = stare_initiala
    litere = 0

    for litera in cuvant:
        for i in range(len(transitions)):
            if transitions[i][0] == stare_curenta and transitions[i][1] == litera:
                litere += 1
                stare_curenta = transitions[i][2]
                break

    stare_finala = 0
    for i in range(len(states)):
        if states[i][0] == stare_curenta:
            if len(states[i]) == 2 and states[i][1] == "F":
                stare_finala += 1
                break
            if len(states[i]) == 3 and states[i][2] == "F":
                stare_finala += 1
                break
    if stare_finala == 0 or litere != len(cuvant):
        print(">>reject")
    else:
        print(">>accept")

def __main__():
    fisier, cuvant = argumente_terminal()
    sigma, states, transitions = citire_fisier(fisier)
    stare_initiala = verificare_fisier(sigma, states, transitions)
    if stare_initiala != -1:
        verificare_dfa(cuvant, stare_initiala, states, transitions)

__main__()
