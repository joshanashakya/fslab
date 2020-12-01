#!/usr/bin/env python

from crispset import CrispSetOp

op = CrispSetOp(['a', 'b', 'c', 'd', 'e'], [{'a':1, 'd':0}, {'c':1, 'a': 1}])
print(op.containment())