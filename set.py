def is_empty(L):
    if L == []:
        return True
    else:
        return False

def FirstElmt(L):
    return L[0]

def Tail(L):
    return L[1:]

def is_member(X,L):
    if is_empty(L):
        return False
    elif X == FirstElmt(L):
        return True
    else:
        return is_member(X,Tail(L))

def konso(s,L):
    if L == []:
        return [s]
    else:
        return [s]+L

def make_set(L):
    if is_empty(L):
        return L
    else:
        if is_member(FirstElmt(L),Tail(L)):
            return make_set(Tail(L))
        else:
            return konso(FirstElmt(L),make_set(Tail(L)))

def is_set(L):
    print(L)
    if is_empty(L):
        return True
    else:
        if is_member(FirstElmt(L),Tail(L)):
            return False
        else:
            return is_set(Tail(L))

