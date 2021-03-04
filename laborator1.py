sigma = []
states = []
transitions = []
errors = 0

with open('file.txt') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace('\n', '')
        lines[i] = lines[i].replace("    ", '')
        #lines[i] = lines[i].replace(',', '')
        lines[i] = lines[i].replace(':', '')
    lines_after_delete = []

    for i in range(len(lines)):
        if lines[i].startswith('#'):
            pass
        else:
            lines_after_delete.append(lines[i])
    lines.clear()
    lines = lines_after_delete

    for i in range ( len ( lines ) ):
        if lines[i].startswith("Sigma"):
            for j in range(i+1,len(lines)):
                if lines[j].startswith("End"):      #Cand intalnim end inseamna ca s-a terminat de citit alfabetul
                    i = j                           # si vom continua de citit restul fisierului
                    break
                else:
                    sigma.append(lines[j])
        elif lines[i].startswith("States"):
            for j in range(i+1,len(lines)):
                if lines[j].startswith("End"):
                    i = j
                    break
                else:
                    states.append(lines[j])
        elif lines[i].startswith("Transitions"):
            for j in range(i+1,len(lines)):
                if lines[j].startswith("End"):
                    i = j
                    break
                else:
                    transitions.append(lines[j])
#Dupa ce terminam de format listele sigma,states si tranzitions urmeaza sa cautam de cate ori apare S si F
#iar apoi sa modificam acelea pentru a scapa de ,S sau ,F
    #print(states)
    #print(sigma)
    noS = 0
    noF = 0
    for s in states:
        if s[len(s) - 1] == 'S':
            noS += 1
        elif s[len(s) - 1] == 'F':
            noF += 1

    if noS == 0:
        print("Nu exista stare de start")
        errors += 1
    elif noS > 1:
        print("Exista prea multe stari de start")
        errors += 1
    if noF == 0:
        print("Nu exista stare finish")
        errors += 1

    for tran in transitions:
        tran = tran.replace(',', " ")
        aux = tran.split()

    #Verificam daca exista prima stare

        gasit = 0
        for i in range(0 , len(states)):
            if states[i].startswith(aux[0]):
                gasit = 1
                break
        if gasit == 0:
            print("Nu s-a gasit starea:"+aux[0]+" in lista de stari")
            errors += 1

    #Verificam daca exista cuvantul

        gasit = 0
        for i in range(0 , len(sigma)):
            if sigma[i].startswith(aux[1]):
                gasit = 1
                break
        if gasit == 0:
            print("Nu s-a gasit cuvantul:"+aux[1]+" in lista de cuvinte")
            errors += 1

    #Verificam daca exista a doua stare

        gasit = 0
        for i in range(0 , len(states)):
            if states[i].startswith(aux[2]):
                gasit = 1
                break
        if(gasit == 0):
            print("Nu s-a gasit starea:"+aux[2]+" in lista de stari")
            errors += 1

    if errors == 0:
        print("Nu aveti erori.")
    else:
        print("Aveti "+str(errors)+" erori.")

