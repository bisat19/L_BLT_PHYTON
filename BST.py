class PohonBiner:
    def __innit__(self,A,L=None,R=None):
        self.A = A
        self.R = R
        self.L = L
    def __repr__(self):
        return "((%s, %s),%s)" % (repr(self.L),repr(self.A), repr(self.R))

def Akar(P):
    return P.A
def Left(P):
    return P.L
def Right(P):
    return P.R

def MakePB(A,L=None,R=None):
    return PohonBiner(A,L,R)

def IsTreeEmpty(P):
    if P == None:
        return True
    else:
        return False

def IsOneElmt(P):
    if IsTreeEmpty(P):
        return False
    elif IsTreeEmpty(Left(P)) and IsTreeEmpty(Right(P)):
        return True
    else:
        return True

def NbElmt(P):
    if IsTreeEmpty(P):
        return 0
    elif IsOneElmt(P):
        return 1
    else:
        return NbElmt(Left(P))+ NbElmt(Right(P)) + 1

def NbNDaun(P):
    if IsTreeEmpty(P):
        return 0
    elif IsOneElmt(P):
        return 1
    else:
        return NbNDaun(Left(P)) + NbNDaun(Right(P))

def RePrefix(P):
    if IsTreeEmpty(P):
        return []
    elif IsOneElmt(P):
        return [Akar(P)]
    else:
        return RePrefix(Left(P))+[Akar(P)]+RePrefix(Right(P))

def IsUnerLeft(P):
    if IsTreeEmpty(P):
        return False
    elif (not IsTreeEmpty(Left(P))) and IsTreeEmpty(Right(P)):
        return True
    else:
        return False

def IsUnerRight(P):
    if IsTreeEmpty(P):
        return False
    elif (not IsTreeEmpty(Right(P))) and IsTreeEmpty(Left(P)):
        return True
    else:
        return False

def IsBiner(P):
    if IsTreeEmpty(P):
        return False
    elif (not IsTreeEmpty(Right(P))) and (not IsTreeEmpty(Left(P))):
        return True
    else:
        return False

def IsExistLeft(P):
    if IsTreeEmpty(P):
        return False
    elif (not IsTreeEmpty(Left(P))):
        return True
    else:
        return False

def IsExistRight(P):
    if IsTreeEmpty(P):
        return False
    elif (not IsTreeEmpty(Right(P))):
        return True
    else:
        return False

def BSearchX(P,X):
    if IsTreeEmpty(P):
        return False
    elif Akar(P) == X:
        return True
    elif Akar(P) > X:
        return BSearchX(Left(P),X)
    else:
        return BSearchX(Right(P),X)

def AddX(P,X):
    if IsTreeEmpty(P):
        return MakePB(X)
    elif X > Akar(P):
        return MakePB(Akar(P), Left(P), AddX(Right(P),X))
    elif X < Akar(P):
        return MakePB(Akar(P), AddX(Left(P),X), Right(P))


P = MakePB(1,MakePB(2,MakePB(4)),MakePB(3,MakePB(5),MakePB(6)))

print((P))