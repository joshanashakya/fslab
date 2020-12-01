#!/usr/bin/env python

import sys
from fuzzyset import FuzzySetOp

def input_domain():
    '''
    Reads elements of the domain.
    '''
    size = int(input('Enter the number of elements in the domain: '))
    print('Enter {} elements: '.format(size))
    domain = [input() for i in range(size)]
    return domain

def is_valid(domain, cset):
    non_zero_elements = [element for element in cset if cset[element] > 0]
    if len(non_zero_elements) > len(domain):
        return False
    invalid_elements = [element for element in cset if (cset[element] > 1) and (element not in domain)]
    if len(invalid_elements) > 0:
        return False
    return True

def input_set(domain):
    '''
    Creates a new set and returns it.
    '''
    size = int(input('Enter the number of elements in the set: '))
    print('Enter {} element and membership value: '.format(size))
    cset = {}
    for i in range(size):
        key = input()
        value = float(input())
        if not (0 <= value <= 1):
            print('Invalid membership value. Please enter the value between 0 and 1 (inclusive).')
            value = int(input())
        cset[key] = value
    if not is_valid(domain, cset):
        print('Invalid set or set size. Please enter elements from the domain.\nX = {}'.format(domain))
        input_set(domain)
    return cset

def show_menu():
    to_print = '''Options
1. (U)nion
2. (I)ntersection
3. (C)omplement
4. (S)ubset
5. (A)lpha-Cut
6. (Q)uit
Enter choice: '''
    while True:
        try:
            choice = input(to_print).strip()[0].lower()
        except (EOFError, KeyboardInterrupt, IndexError):
            choice = 'q'
        print('Your choice: {}'.format(choice))
        if choice not in 'uicsaq':
            print('Invalid choice. Try again.')
        else:
            break
    return choice

def main_method(domain, set1, set2):
    print('X = {}'.format(domain))
    print('A = {}'.format(set1))
    print('B = {}'.format(set2))
    obj = FuzzySetOp(domain, [set1, set2])
    while True:
        choice = show_menu()
        if choice == 'q':
            print('YOU QUIT!!!!!')
            break
        eqs = '=' * 50
        if choice == 'u':
            output = obj.union()
            print('\n{}\nOutput\n{}'.format(eqs, eqs))
            print('Union\nA = {}\nB = {}\nA \u222A B = {}'.format(set1, set2, output))
        elif choice == 'i':
            output = obj.intersection()
            print('\n{}\nOutput\n{}'.format(eqs, eqs))
            print('Intersection\nA = {}\nB = {}\nA \u2229 B = {}'.format(set1, set2, output))
        elif choice == 'c':
            output = obj.complement()
            print('\n{}\nOutput\n{}'.format(eqs, eqs))
            print('Complement\nA = {}\nA` = {}\nB = {}\nB` = {}'.format(set1, output[0], set2, output[1]))
        elif choice == 's':
            output = obj.containment()
            print('\n{}\nOutput\n{}'.format(eqs, eqs))
            print('Containment\nA = {}\nB = {}. \nA is {}subset of B.'.format(set1, set2, '' if output else 'not '))
        elif choice == 'a':
            alpha = float(input('Enter the value of alpha: '))
            output = obj.alphacut(alpha)
            print('\n{}\nOutput\n{}'.format(eqs, eqs))
            print('Alpha-Cut ({})\nA = {}\nA_{} = {}\nB = {}\nB_{} = {}'.format(alpha, set1, alpha, output[0], set2, alpha, output[1]))
        print('{}\n'.format(eqs))

def parse(data):
    elements = data.split(' ')
    cset = {}
    for element in elements:
        pair = element.split(':')
        key = pair[0]
        value = float(pair[1])
        cset[key] = value
    return cset

def input_file(filename):
    fobj = open(filename, mode = 'r')
    data = [line.strip() for line in fobj.readlines()]
    fobj.close()
    domain = data[0].split(' ')
    set1 = parse(data[1])
    set2 = parse(data[2])
    main_method(domain, set1, set2)

def input_cli():
    domain = input_domain()
    set1 = input_set(domain)
    set2 = input_set(domain)
    main_method(domain, set1, set2)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        input_cli()
    else:
        input_file(sys.argv[1])