#class Pohon Biner
class PohonBiner:
    def __init__(self, A, L=None, R=None):
        self.A = A
        self.L = L
        self.R = R
    def __repr__(self):
        return "((%s, %s), %s)" % (repr(self.L), repr(self.A), repr(self.R))

def Akar(P):
    return P.A
def Left(P):
    return P.L
def Right(P):
    return P.R

def MakePB(A, L=None, R=None):
    return PohonBiner(A, L, R)

def IsTreeEmpty(P):
    if P == None:
        return True
    else:
        return False

#Fungsi IsOneElmt 
#IsOneElmt : PohonBiner -> Boolean
#IsOneElmt(P) = True jika P adalah pohon biner dengan satu elemen
def IsOneElmt(P):
    if IsTreeEmpty(P):
        return False
    elif IsTreeEmpty(Left(P)) and IsTreeEmpty(Right(P)):
        return True
    else:
        return False
#Fungsi NBElmt
#NBElmt : PohonBiner -> Integer
#NBElmt(P) = banyaknya elemen pada pohon biner P
def NBElmt(P):
    if IsTreeEmpty(P):
        return 0
    elif IsOneElmt(P):
        return 1
    else:
        return NBElmt(Left(P)) + NBElmt(Right(P)) + 1

#Fungsi NbDaun
#NbDaun : PohonBiner -> Integer
#NbDaun(P) = banyaknya daun pada pohon biner P
def NbDaun(P):
    if IsTreeEmpty(P):
        return 0
    elif IsOneElmt(P):
        return 1
    else:
        return NbDaun(Left(P)) + NbDaun(Right(P))

#ReRefix
#ReRefix : PohonBiner -> ListofElement
#ReRefix(P) = list elemen-elemen pada pohon biner P
def Inorder(P):
    if IsTreeEmpty(P):
        return []
    elif IsOneElmt(P):
        return [Akar(P)]
    else:
        return Inorder(Left(P)) + [Akar(P)] + Inorder(Right(P))

def Prefix(P):
    if IsTreeEmpty(P):
        return []
    elif IsOneElmt(P):
        return [Akar(P)]
    else:
        return [Akar(P)]+ [Prefix(Left(P))] + [Prefix(Right(P))]

def Postfix(P):
    if IsTreeEmpty(P):
        return []
    elif IsOneElmt(P):
        return [Akar(P)]
    else:
        return Postfix(Left(P)) + Postfix(Right(P)) + [Akar(P)]
#isUnerLeft
#isUnerLeft : PohonBiner -> Boolean
#isUnerLeft(P) = True Kiri Tidak Kosong
def isUnerLeft(P): 
    if IsTreeEmpty(P):
        return False
    elif (not IsTreeEmpty(Left(P)) and IsTreeEmpty(Right(P))):
        return True
    else:
        return False

#isUnerRight
#isUnerRight : PohonBiner -> Boolean
#isUnerRight(P) = True Kanan Tidak Kosong
def isUnerRight(P):
    if IsTreeEmpty(P):
        return False
    elif (IsTreeEmpty(Left(P)) and not IsTreeEmpty(Right(P))):
        return True
    else:
        return False

#fungsi isBiner
#isBiner : PohonBiner -> Boolean
#isBiner(P) = True jika P adalah pohon biner (mengandung sub pohon kiri dan kanan)
def isBiner(P):
    if IsTreeEmpty(P):
        return False
    elif (not IsTreeEmpty(Left(P)) and not IsTreeEmpty(Right(P))):
        return True
    else:
        return False

#fungsi IsExistLeft
#IsExistLeft : PohonBiner -> Boolean
#IsExistLeft(P) = True jika P adalah pohon biner dengan sub pohon kiri
def IsExistLeft(P):
    if (not IsTreeEmpty(P) and not IsTreeEmpty(Left(P))):
        return True
    else:
        return False

#fungsi IsExistRight
#IsExistRight : PohonBiner -> Boolean
#IsExistRight(P) = True jika P adalah pohon biner dengan sub pohon kanan
def IsExistRight(P):
    if (not IsTreeEmpty(P) and not IsTreeEmpty(Right(P))):
        return True
    else:
        return False

# =================================================================================================#
# BINARY SEARCH TREE 

#Fungsi BSearchX
#BSearchX : PohonBiner, Element -> Boolean
#BSearchX(P, X) = True jika X adalah elemen pada pohon biner P
def BSearchX(P, X):
    if IsTreeEmpty(P):
        return False
    elif Akar(P) == X:
        return True
    elif Akar(P) > X:
        return BSearchX(Left(P), X)
    else:
        return BSearchX(Right(P), X)

#fungsi AddX(P, X)
#AddX : PohonBiner, Element -> PohonBiner
#AddX(P, X) = Pohon biner yang merupakan hasil penambahan elemen X pada pohon biner P
def AddX(P, X):
    if IsTreeEmpty(P):
        return MakePB(X)
    elif X>Akar(P):
        return MakePB(Akar(P), Left(P), AddX(Right(P), X))
    elif X<Akar(P):
        return MakePB(Akar(P), AddX(Left(P), X), Right(P))
    else:
        return P


def max(P):
    if IsTreeEmpty(P):
        return 0
    elif IsOneElmt(P):
        return Akar(P)
    else:
        Right(P)

PB = MakePB(5, MakePB(3, MakePB(2, MakePB(1)), MakePB(4, MakePB(4))), MakePB(6, MakePB(7, MakePB(6), MakePB(7,MakePB(8)))))
#print(BSearchX(PB, 31))
#print(ReRefix(PB))
#print(PB)
# p = MakePB(1, MakePB(2, MakePB(4)), MakePB(3, MakePB(5), MakePB(6)))
# print(NBElmt(p))
# print(NbDaun(p))
# print(ReRefix(p))
print(NBElmt(PB))
print(NbDaun(PB))
print(max(PB))