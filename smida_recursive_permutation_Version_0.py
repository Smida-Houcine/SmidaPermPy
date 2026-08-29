# ======================================================================
# Smida's Row Insertion Permutation Algorithm (RIPA)
# Recursive version
# ======================================================================
# Written by: SMIDA Houcine L. (2026)
# Recursive row insertion permutation algorithm for generating all permutations.
# The elements of the input array must be distinct.
# ======================================================================
'''
RIPA generates permutations progressively by inserting a new row
into the previously generated permutation array at every possible
position and filling the inserted row with the new element.
'''

# ======================================================================
# Define the input array
# ======================================================================
Tab = [1, 2, 3, 4]
# ======================================================================
# Recursive row insertion permutation algorithm
# ======================================================================
def Smida_Permutation(E, n):
    # ------------------------------------------------------------------
    # Base case: n = 0
    # The empty array has exactly one permutation: [].
    # ------------------------------------------------------------------
    if n == 0:
        return [[]]
    # ------------------------------------------------------------------
    # Base case: n = 1
    # The only permutation contains the first element: Tab[0].
    # ------------------------------------------------------------------
    if n == 1:
        return [[Tab[n - 1]]]
    # ------------------------------------------------------------------
    # Recursively generate all permutations of the first n - 1 elements.
    # ------------------------------------------------------------------
    E = Smida_Permutation(E, n - 1)
    # ------------------------------------------------------------------
    # F stores the complete permutation array generated at the
    # current recursive level.
    # ------------------------------------------------------------------
    F = []
    # ------------------------------------------------------------------
    # Row insertion:
    # Insert the new element Tab[n - 1] at every possible position.
    # ------------------------------------------------------------------
    for i in range(n):
        # Create a copy of the previously generated permutation array
        # to form the current permutation block Bi.
        Bi = [P[:] for P in E]
        # Fill every row of the current block with the new element
        # by inserting it at position i.
        for P in Bi:
            P.insert(i, Tab[n - 1])
        # Append the complete block Bi to the final permutation array F.
        F.extend(Bi)
    # ------------------------------------------------------------------
    # Return all permutations generated at the current recursive level.
    # ------------------------------------------------------------------
    return F
# ======================================================================
# Generate all permutations of the input array
# ======================================================================
TabPerm = Smida_Permutation(Tab, len(Tab))
# ======================================================================
# Display all generated permutations
# ======================================================================
for perm in TabPerm:
    print(perm)
# ======================================================================
# End of Smida's Row Insertion Permutation Algorithm (RIPA)
# ======================================================================
