

def posiziona(lettera, string):
    string = list(string)
    rang = range(len(string) +1)
    lista = []
    for j in rang:
        d = string[:]
        d.insert(j, lettera)
        lista.append(''.join(d))
    return lista


string = 'abcd'
def an(s):
    angs = []
    s = list(s)
    for l in s:
        o = []
        if len(angs) == 0:
            angs.append([l])
        else:
            for e in angs:
                er = posiziona(l, e)
                o += er
                angs = o
    print(angs)

an(string)

