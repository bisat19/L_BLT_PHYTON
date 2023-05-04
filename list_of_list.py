# ===============================================
def isEmptyLOL(S):
    return S == []

def tailList(S):
    return S[1:]

def nb_elmt(L):
    if L == []:
        return 0
    else:
        return 1+nb_elmt(L[1:])

def isAtom(S):
    return not(isEmptyLOL(S)) and (jumlahkartu(S) == 1) and not isinstance(S,list)

def isList(S):
    return not(isAtom(S))

def jumlahkartu(S):
    if isinstance(S, list):
        if isEmptyLOL(S):
            return 0
        else:
            return 1 + jumlahkartu(tailList(S))
    else:
        return 1

def isOneElmt(S):
    return jumlahkartu(S) == 1
# ===============================================
def konsoLOL(x, S):
    if isEmptyLOL(S):
        return [x]
    else:
        return [x] + S

def konsiLOL(x, S):
    if isEmptyLOL(S):
        return [x]
    else:
        return S + [x]
# ===============================================
def firstList(S):
    if isinstance(S, list):
        return S[0]
    else:
        return S

def tailList(S):
    return S[1:]

def lastList(S):
    return S[-1]

def headList(S):
    return S[:-1]
# ===============================================
def isEqS(S1, S2):
    if isEmptyLOL(S1) and isEmptyLOL(S2):
        return True
    elif not(isEmptyLOL(S1)) and not(isEmptyLOL(S2)):
        if isAtom(firstList(S1)) and isAtom(firstList(S2)):
            return (firstList(S1) == firstList(S2)) and isEqS(tailList(S1), tailList(S2))
        elif isList(firstList(S1)) and isList(firstList(S2)):
            return isEqS(firstList(S1), firstList(S2)) and isEqS(tailList(S1), tailList(S2))
        else:
            return False
    else:
        return False

def isMemberS(a, S):
    if isEmptyLOL(S):
        return False
    else:
        if isAtom(firstList(S)):
            return a == firstList(S) or isMemberS(a, tailList(S))
        elif isList(firstList(S)):
            return isMemberS(a, firstList(S)) or isMemberS(a, tailList(S))

def isMemberLS(L, S):
    if isEmptyLOL(L) and isEmptyLOL(S):
        return True
    elif not(isEmptyLOL(L)) and not(isEmptyLOL(S)):
        if isAtom(firstList(S)):
            return isMemberLS(L, tailList(S))
        else:
            if isEqS(L, firstList(S)):
                return True
            else:
                return isMemberLS(L, tailList(S))
    else:
        return False

def rember(a, S):
    if isEmptyLOL(S):
        return S
    else:
        if isAtom(firstList(S)):
            if a == firstList(S):
                return rember(a, tailList(S))
            else:
                return konsoLOL(firstList(S), rember(a, tailList(S)))
        else:
            return konsoLOL(firstList(S), rember(a, tailList(S)))

def max2(a, b):
    if a >= b:
        return a
    else:
        return b

def max(S):
    if isOneElmt(S):
        if isAtom(S):
            return firstList(S)
        else:
            return max(firstList(S))
    else:
        if isAtom(firstList(S)):
            return max2(firstList(S), max(tailList(S)))
# max2(1, max2(2, max2(3, max2(max(4, 5), max2(9, 10)))))
        else:
            return max2(max(firstList(S)), max(tailList(S)))
