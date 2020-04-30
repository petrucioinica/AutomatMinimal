def filltable():
    global minimizare,limbaj,stari,finale,tranzitii,initiala
    ok = 0
    for i in range(len(stari)):
        for j in range(len(stari)):
            if i > j:
                for w in limbaj:
                    if minimizare[i][j] != 1:
                        for tr in tranzitii:
                            if tr[0] == stari[i] and tr[2] == w:
                                q0 = tr[1]
                            if tr[0] == stari[j] and tr[2] == w:
                                q1 = tr[1]
                        for a in range(len(stari)):
                            if q0 == stari[a]:
                                q0 = a
                            if q1 == stari[a]:
                                q1 = a
                        if minimizare[max(q0,q1)][min(q0,q1)] == 1:
                            ok = 1
                            minimizare[i][j] = 1
    return ok


limbaj = ["a"]
stari = ["0","1","2","3","4","5","6","7"]
finale = ["7"]
tranzitii = [("0","1","a"),
            ("1","2","a"),
            ("2","3","a"),
            ("3","4","a"),
            ("4","5","a"),
            ("5","6","a"),
            ("6","7","a"),
            ("7","7","a")]
initiala = "0"


minimizare = [[0]*len(stari) for i in range(len(stari)) ]
for i in range(len(stari)):
    for j in range(len(stari)):
        if stari[i] in finale and stari[j] not in finale:
            minimizare[max(i,j)][min(i,j)] = 1


while filltable() != 0:
   filltable()

stariechivalente=[]
for i in range(len(stari)):
    for j in range(len(stari)):
        if i > j:
            if minimizare[i][j] == 0:
                stariechivalente.append({(stari[j]),(stari[i])})
for i in stariechivalente:
    for j in stariechivalente:
        ok = 0
        for k in j:
            if k in i:
                ok = 1
        if ok == 1:
            for k in j:
                i.update(j)
echivalente1 = []
for i in stariechivalente:
    if i not in echivalente1:
        echivalente1.append(i)
for i in range(len(echivalente1)):
    echivalente1[i] = list(echivalente1[i])
stariminimal=[]
for i in stari:
    ok = 1
    for j in echivalente1:
        if i in j:
            ok = 0
    if ok == 1:
        stariminimal.append(i)
for i in echivalente1:
    stare=""
    for j in i:
        stare=stare+j
    stariminimal.append(stare)
tranzitiiminimal = []
tranzitii1 = []
finaleminimal = []
for tr in tranzitii:
    mnm=0
    fin=0
    for i in stariminimal:
        if tr[0] in i:
            x = i
        if tr[0] in initiala:
            mnm=1
        if tr[0] in finale:
            fin=1
        if tr[1] in i:
            y = i
    tranzitii1.append((x,y,tr[2]))
    if mnm == 1:
        initialaminimal = x
    if fin == 1:
        finaleminimal.append(x)
for i in tranzitii1:
    if i not in tranzitiiminimal:
        tranzitiiminimal.append(i)

for i in minimizare:
    print(i)

print()

finaleminimal1=[]
for i in finaleminimal:
    if i not in finaleminimal1:
        finaleminimal1.append(i)
print("Automatul minimal:")
print("Limbaj:",end=" ")
print(limbaj)
print("starile sunt: ",end=" ")
print(stariminimal)
print("Stari finale: ",end=" ")
print(finaleminimal1)
print("Stare initiala: ",end=" ")
print(initialaminimal)
print("Tranzitii: ")
for i in tranzitiiminimal:
    print("    ",end=" ")
    print(i)




