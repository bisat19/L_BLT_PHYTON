from Tree import *
from list_of_list import *
from set import *

PB = MakePB(5, MakePB(3, MakePB(2, MakePB(1)), MakePB(4, MakePB(4))), MakePB(6, MakePB(7, MakePB(6), MakePB(7,MakePB(8,MakePB(9))))))
#visual
print(Prefix(PB))
#Hasil data
def Hasil_data(t):
    if NBElmt(Left(t))>NBElmt(Right(t)):
        return("Pohon menunjukkan bahwa film dalam negeri lebih diminati")
    elif NBElmt(Left(t))<NBElmt(Right(t)):
        return("Pohon menunjukkan bahwa film luar negeri lebih diminati")
    else:
        return("Pohon menunjukkan bahwa baik film dalam maupun luar negeri sama sama diminati")
print(Hasil_data(PB))

#list of list to list
K = Prefix(PB)
S = []
def simplifier(L):
    if isEmptyLOL(L):
        return S
    else:
        if isAtom(firstList(L)):
            S.append(firstList(L))
            return simplifier(tailList(L))
        elif isList(firstList(L)):
            simplifier(firstList(L))
            return simplifier(tailList(L))
R = simplifier(K)

#list to set
def make_set_movie(L):
    if is_empty(L):
        return L
    else:
        if is_member(FirstElmt(L),Tail(L)):
            return make_set_movie(Tail(L))
        else:
            return konso(FirstElmt(L),make_set_movie(Tail(L)))        
print(make_set_movie(R))

#list nama film dalam data
'''code_movie = lambda x :f"Ada apa dengan Cinta?" if x == 1 else
(f"Nanti Kita Cerita Tentang Hari Ini" if x == 2 else (f"Dilan 1990" if x == 3
else (f"Imperfect" if x == 4 else (f"LA LA LAND" if x == 6 
else (f"Purple Hearts" if x == 7 else (f"Us" if x == 8 
else(f"Five Feet Apart" if x == 9 )))))))'''

c1 = lambda x:f"Ada apa dengan Cinta?" if x == 1 else c2
c2 = lambda x:f"Nanti Kita Cerita Tentang Hari Ini" if x == 2 else c3
c3 = lambda x:f"Dilan 1990" if x == 3 else c4
c4 = lambda x:f"Imperfect" if x == 4 else c6
c6 = lambda x:f"LA LA LAND" if x == 6 else c7
c7 = lambda x:f"Purple Hearts" if x == 7 else c8
c8 = lambda x:f"Us" if x == 8 else c9
c9 = lambda x:f"Five Feet Apart" if x == 9 else c5
c5 = lambda x:f"bukan film" if x == 4 else "bukan code"

#print(c4(8))

def code_to_movie (L):
    if is_empty(L):
        return L
    else:
        if FirstElmt(L) == 1:
            return konso(c1(FirstElmt(L)),code_to_movie(Tail(L)))
        elif FirstElmt(L) == 2:
            return konso(c2(FirstElmt(L)),code_to_movie(Tail(L)))
        elif FirstElmt(L) == 3:
            return konso(c3(FirstElmt(L)),code_to_movie(Tail(L)))
        elif FirstElmt(L) == 4:
            return konso(c4(FirstElmt(L)),code_to_movie(Tail(L)))
        elif FirstElmt(L) == 6:
            return konso(c6(FirstElmt(L)),code_to_movie(Tail(L)))
        elif FirstElmt(L) == 7:
            return konso(c7(FirstElmt(L)),code_to_movie(Tail(L)))
        elif FirstElmt(L) == 8:
            return konso(c8(FirstElmt(L)),code_to_movie(Tail(L)))
        elif FirstElmt(L) == 9:
            return konso(c9(FirstElmt(L)),code_to_movie(Tail(L)))
        else:
            return code_to_movie(Tail(L))

print(code_to_movie(make_set_movie(R)))
        
