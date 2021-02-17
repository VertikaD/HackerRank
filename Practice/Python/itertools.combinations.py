#code by Vertika Dhingra.
from itertools import combinations
from itertools import chain

S,k = input().split()
S_sort = sorted(S)

comb=[]
for i in range(1,int(k)+1):
    comb.append(list(combinations(S_sort,i)))

comb2 = list(chain.from_iterable(comb)) #list flattening.
for x in comb2:
    print(*x,sep='')
