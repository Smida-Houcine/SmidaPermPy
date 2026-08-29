# SmidaPermPy

Implementation of Smida's Row Insertion Permutation Algorithm (RIPA) for generating all permutations in Python.

## Description

This repository contains implementations of **Smida's Row Insertion Permutation Algorithm (RIPA)** for generating all permutations of an array whose elements are distinct.

Two approaches are provided:

* Iterative row insertion permutation
* Recursive row insertion permutation

RIPA generates permutations progressively by inserting a new row at every possible position in the previously generated permutation array and filling the inserted row with the new element.

## Files

### Iterative Row Insertion Permutation

* `smida_iterative_permutation_Version_0.py`
* `smida_iterative_permutation.py`
* `SmidaPermPy.py`

### Recursive Row Insertion Permutation

* `smida_recursive_permutation_Version_0.py`
* `smida_recursive_permutation.py`
* `SmidaPermPy_recursive.py`

## Requirements

* Python 3

No external libraries are required.

## Input

The program allows the user to enter elements separated by spaces.

The elements must be distinct.

The number of elements must not exceed 10.

The elements can be:

* integers
* characters
* words
* sentences

Sentences containing spaces must be enclosed in double quotes (`" "`).

### Integers

`1 2 3 4`

### Characters

`A B C D`

### Words

`Blue Green Red Yellow`

### Sentences

`"Drink more water" "Get regular exercise" "Sleep better"`

## Example

For the input:

`1 2 3`

the program generates all permutations:

`[3, 2, 1]`  
`[3, 1, 2]`  
`[2, 3, 1]`  
`[1, 3, 2]`  
`[2, 1, 3]`  
`[1, 2, 3]`

The number of generated permutations is:

`3! = 6`

## Citation

SMIDA, Houcine L., *RIPA: An Iterative Row Insertion Algorithm for Permutation Generation* (December 12, 2025). DOI: http://dx.doi.org/10.2139/ssrn.604925

## Author

Written by: SMIDA Houcine L. (2026)
