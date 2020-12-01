#!/usr/bin/env python

X = []

def merge_sets(set1, set2):
    merge = {}
    merge.update(set1)
    merge.update(set2)
    return merge

def union(A, B):
    union = {}
    all_elements = merge_sets(A, B)
    for element in all_elements:
        chi_A = A[element] if element in A else 0
        chi_B = B[element] if element in B else 0
        chi_element = max(chi_A, chi_B)
        if chi_element == 1:
            union[element] = 1
    return union

def intersection(A, B):
    intersection = {}
    all_elements = merge_sets(A, B)
    for element in all_elements:
        chi_A = A[element] if element in A else 0
        chi_B = B[element] if element in B else 0
        chi_element = min(chi_A, chi_B)
        if chi_element == 1:
            intersection[element] = 1
    return intersection

def set_complement(c_set):
    complement_cset = {}
    for element in X:
        chi_cset = c_set[element] if element in c_set else 0
        chi_element = 1 - chi_cset
        if chi_element == 1:
            complement_cset[element] = 1
    return complement_cset

def complement(A, B):
    return [set_complement(A), set_complement(B)]

def containment(A, B):
    flag = True
    for element in A:
        chi_A = A[element]
        chi_B = B[element] if element in B else 0
        if chi_A <= chi_B:
            continue
        else:
            flag = False
    return flag

def is_valid(c_set):
    flag = True
    for element in c_set:
        if (c_set[element] == 1) and (element not in X):
            flag = False
            break
    return flag

def input_universe():
    '''
    Reads elements of the universe set and appends the elements to the universe set.
    '''
    universe_size = int(input('Enter the number of elements of the universe: '))
    print('Enter {} elements: '.format(universe_size))
    for i in range(universe_size):
        X.append(input())

def input_set():
    '''
    Creates a new set and returns it.
    '''
    set_size = int(input('Enter the number of elements of the set: '))
    print('Enter {} (element, membership): '.format(set_size))
    c_set = {}
    for i in range(set_size):
        key = input()
        value = int(input())
        if value not in [0, 1]:
            print('Invalid membership value. Please enter 0 or 1.')
            value = int(input())
        c_set[key] = value
    if not is_valid(c_set):
        print('Invalid set. Please enter elements from domain {} only.'.format(X))
        input_set()
    return c_set

def print_output(output, choice):
    if choice == 'u':
        to_print = 'Union of two sets\n{}\n\n'.format(output)
    elif choice == 'i':
        to_print = 'Intersection of two sets\n{}\n\n'.format(output)
    elif choice == 'c':
        to_print = 'Complement of the first set\n{}\nComplement of the second set\n{}\n\n'.format(output[0], output[1])
    elif choice == 'o':
        to_print = 'The first set is {}contained in the second set.\n\n'.format('not ' if output is False else '')
    print(to_print)

UNICO = {'u': union, 'i': intersection, 'c': complement, 'o': containment}

def show_menu(A, B):
    to_print = '''Options
1. (U)nion
2. (I)ntersection
3. (C)omplement
4. C(O)ntainment
5. (Q)uit
Enter choice: '''
    while True:
        while True:
            try:
                choice = input(to_print).strip()[0].lower()
            except (EOFError, KeyboardInterrupt, IndexError):
                choice = 'q'
            print('Your choice: {}'.format(choice))
            if choice not in 'uicoq':
                print('Invalid choice. Try again.')
            else:
                break
        if choice == 'q':
            break
        output = UNICO[choice](A, B)
        print_output(output, choice)


def main_method():
    input_universe()
    A = input_set()
    B = input_set()
    show_menu(A, B)

if __name__ == '__main__':
    main_method()