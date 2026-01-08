"""
Smida's Row Insertion Permutation Algorithm
Generates all permutations iteratively
Tab: input array with n distinct elements
"""
from typing import List, Any
Tab: List[Any] = [1,2,3,4]
def Smida_Permutation(E: List[Any], n: int) -> None:
    if n == 0:
        print(E)
        return
    E = [[Tab[0]]]
    if n == 1:
        print(E)
        return
    for g in range(1, n):
        F = []
        for i in range(g+1):
            Bi = [P[:] for P in E]
            for P in Bi:
                P.insert(i, Tab[g])
            F.extend(Bi)
        E = F
    for perm in E:
        print(perm)
Smida_Permutation(Tab,len(Tab))