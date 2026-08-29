Tab = [1, 2, 3, 4]
def Smida_Permutation(E, n):
    if n == 0:
        return [[]]

    if n == 1:
        return [[Tab[0]]]

    E = Smida_Permutation(E, n - 1)
    
    F = []
    
    for i in range(n):
        Bi = [P[:] for P in E]
        for P in Bi:
            P.insert(i, Tab[n - 1])
        F.extend(Bi)
    
    return F

TabPerm = Smida_Permutation(Tab, len(Tab))
for perm in TabPerm:
    print(perm)
