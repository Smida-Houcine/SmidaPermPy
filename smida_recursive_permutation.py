"""
Written by: SMIDA Houcine L. (2026)

Smida's Row Insertion Permutation Algorithm (RIPA).

Recursive row insertion permutation algorithm for generating all permutations.

The elements of the array must be distinct.

The elements can be integers, characters, words, or sentences.

If sentences are to be treated as individual elements,
they must be enclosed in double quotes (" ").

Examples:
    1 2 3 4
    A B C D
    Blue Green Red Yellow
    "Drink more water" "Get regular exercise" "Sleep better"
"""

# ================================================================
# Begin recursive row insertion permutation
# ================================================================
def Smida_Permutation(E, n):
    # ------------------------------------------------------------------
    # Base case: n = 1
    # The only permutation contains the first element: Tab[0].
    # ------------------------------------------------------------------
    if n == 1:
        return [[Tab[0]]]
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
        # Insert the new row at position i in each permutation
        # of the current block and fill the inserted row with Tab[n - 1].
        for P in Bi:
            P.insert(i, Tab[n - 1])
        # Append the complete block Bi to the final permutation array F.
        F.extend(Bi)
    # ------------------------------------------------------------------
    # Return all permutations generated at the current recursive level.
    # ------------------------------------------------------------------
    return F
# ================================================================
# End recursive row insertion permutation
# ================================================================

# ================================================================
# Display the purpose of the program
# ================================================================
print("Smida's Row Insertion Permutation Algorithm (RIPA)")
print("Written by: SMIDA Houcine L. (2026)")
print()

# ================================================================
# Read the elements entered by the user
# ================================================================
def read_elements(input_text):
    parsed_elements = []
    current = ""
    quoted = False
    # Spaces separate the elements.
    # Spaces inside " " are part of the current element.
    for character in input_text:
        # A double quote marks the beginning or the end
        # of an element containing spaces.
        if character == '"':
            quoted = not quoted
        # A space separates elements only when it is outside " ".
        elif character.isspace() and quoted == False:
            if current:
                parsed_elements.append(current)
                current = ""
        # All other characters are added to the current element.
        else:
            current = current + character
    # Check for an unclosed pair of double quotes.
    if quoted == True:
        print("\nError: invalid double quotes.")
        exit()
    # Add the last element.
    if current:
        parsed_elements.append(current)
    return parsed_elements

# ================================================================
# Ask the user to enter the elements of the array
# ================================================================
# Spaces separate the elements.
# Spaces inside double quotes (" ") do not separate the elements.
# Double quotes (" ") are used only as delimiters.
values = input(
    "Enter the elements separated by spaces "
    '(use double quotes for sentences): '
)

# ================================================================
# Check the input
# ================================================================
# Check if the input contains at least one element.
if len(values.strip()) == 0:
    print("\nError: the array must contain at least one element.")
    exit()

# ================================================================
# Read and check the elements
# ================================================================
# Read the elements entered by the user.
elements = read_elements(values)
# Count the number of elements.
number_of_elements = len(elements)
# The number of elements must not exceed 10.
if number_of_elements > 10:
    print("\nError: the number of elements must not exceed 10.")
    exit()

# ================================================================
# Check that the elements are distinct
# ================================================================
# set(elements) contains only distinct elements.
# If its length differs from the original number of elements,
# at least two elements are identical.
if len(set(elements)) != number_of_elements:
    print("\nError: all elements must be distinct.")
    exit()

# ================================================================
# Check whether all elements are integers
# ================================================================
# Assume that all elements are integers.
all_integers = True
# Check each element by trying to convert it to an integer.
for item in elements:
    try:
        int(item)
    except ValueError:
        # The element is not an integer.
        all_integers = False
        break

# ================================================================
# Create the input array
# ================================================================
# Use the parsed elements as the input array.
Tab = elements

# ================================================================
# Convert integer elements from strings to integers
# ================================================================
# If all elements are integers, convert them from strings to integers.
# For example: ['1', '2', '3'] becomes [1, 2, 3].
if all_integers:
    Tab = [int(element) for element in Tab]

# ================================================================
# Display the input array
# ================================================================
print(f"\nInput array: {Tab}")

# ================================================================
# Display the number of elements and permutations
# ================================================================
# The number of permutations is n!.
number_of_permutations = 1
for factor in range(1, number_of_elements + 1):
    number_of_permutations = number_of_permutations * factor
print(f"\nNumber of elements: n = {number_of_elements}")
print(
    f"Number of permutations: "
    f"{number_of_elements}! = {number_of_permutations}"
)

# ================================================================
# Generate and display all the permutations
# ================================================================
print("\nPermutations generated by RIPA:")
# Generate and return all permutations recursively.
TabPerm = Smida_Permutation(Tab, number_of_elements)
# Display each generated permutation.
for perm in TabPerm:
    print(perm)

# ================================================================
# End
# ================================================================