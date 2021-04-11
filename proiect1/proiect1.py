def citire_input(file):

    f = open(file)
    # citim numarul de noduri si numarul muchii
    dimensiuni = [int(d) for d in f.readline().strip("\t\n").split(" ")]
    nr_muchii = dimensiuni[1]
    muchii = []
    for i in range(nr_muchii):
        muchie = f.readline().strip("\t\n").replace(" ", "")
        muchii.append(muchie)

    # citim nodurile S si F
    stare_s = f.readline().strip("\t\n").replace(" ", "")
    stare_f = f.readline().strip("\t\n").split(" ")
    stare_f.pop(0)
    # citim numarul de cuvinte din fisierul test
    nr_cuv = int(f.readline())
    # citim cuvintele din fisierul test
    cuv = []
    for i in range(nr_cuv):
        cuv.append(f.readline().strip("\t\n"))
    f.close()
    return muchii, stare_s, stare_f, cuv

def verificare_dfa(cuv, stare_s, stare_f, muchii):
    stare_curenta = stare_s
    contor = 0 # 0 litere au fost procesate pana acum
    drum = [stare_curenta]
    # verificam daca exista drum catre nodul final
    for litera in cuv:
        # luam fiecare litera din cuvant si verificam daca exista o muchie care sa proceseze litera curenta
        # trecem la nodul aflat in capatul urmator muchiei respective
        for i in range(len(muchii)):
            if muchii[i][0] == stare_curenta and muchii[i][2] == litera:
                contor += 1
                stare_curenta = muchii[i][1]
                drum.append(stare_curenta)
                break

    # verificam rezultatul (starea finala si daca toate literele au fost prelucrate)
    if stare_curenta in stare_f and contor == len(cuv):
        return True, drum
    else:
        return False, drum

def __main__():

    # citim DFA-ul si cuvintele din fisier
    muchii, stare_s, stare_f, cuvinte = citire_input("input.in")
    # verificam cuvintele din fisier printr-un DFA
    for cuv in cuvinte:
        rezultat, drum = verificare_dfa(cuv, stare_s, stare_f, muchii)
        if rezultat is False:
            print("NU")
        else:
            print("DA")
            d = " ".join([str(nod) for nod in drum])
            print("Traseu: " + d )

__main__()
