
alph = 'abcdefghijklmnopqrstuvwxyz'


def next(val):

    id = 7
    while id > 0:
        if val[id] == 'z':
            val = val[:id] + 'a' + val[id+1:]
            id -= 1
        else:
            #print("coucou ", alph[alph.find(val[id]) + 1])
            val = val[:id] + alph[alph.find(val[id]) + 1] + val[id+1:]
            break

    return val


# Three successive letters in alphabet
def rule1(val):
    id = 0
    while id < 6:
        if alph.find(val[id:id+3]) >= 0:
            return True
        else:
            id += 1
    return False

# Not 'i', 'o' or 'l'


def rule2(val):
    if 'i' in val or 'o' in val or 'l' in val:
        return False
    return True

# Find two pairs not overlapping


def rule3(val):
    cnt = 0
    i = 0
    while i < 7:
        if val[i] == val[i+1]:
            cnt += 1
            i += 1
        if cnt == 2:
            return True

        i += 1
    return False


if __name__ == '__main__':
    val = 'hepxcrrq'
    while not (rule2(val) and rule1(val) and rule3(val)):
        val = next(val)

    print(val)

    val = next(val)
    while not (rule2(val) and rule1(val) and rule3(val)):
        val = next(val)
    print(val)
