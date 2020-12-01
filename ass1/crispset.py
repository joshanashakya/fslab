'''
Class to perform crisp set operations: union, intersection, complement, and containment.
'''

class CrispSetOp:

    def __init__(self, domain, sets):
        self.domain = domain
        self.sets = sets

    def merge_sets(self):
        merged_set = {}
        for element in self.sets:
            merged_set.update(element)
        return merged_set

    def union(self):
        union = {}
        elements = self.merge_sets()
        for element in elements:
            chi_set1 = self.sets[0][element] if element in self.sets[0] else 0
            chi_set2 = self.sets[1][element] if element in self.sets[1] else 0
            chi_element = max(chi_set1, chi_set2)
            if chi_element == 1:
                union[element] = 1
        return union

    def intersection(self):
        intersection = {}
        elements = self.merge_sets()
        for element in elements:
            chi_set1 = self.sets[0][element] if element in self.sets[0] else 0
            chi_set2 = self.sets[1][element] if element in self.sets[1] else 0
            chi_element = min(chi_set1, chi_set2)
            if chi_element == 1:
                intersection[element] = 1
        return intersection

    def complement_set(self, cset):
        comp_cset = {}
        for element in self.domain:
            chi_cset = cset[element] if element in cset else 0
            chi_element = 1 - chi_cset
            if chi_element == 1:
                comp_cset[element] = 1
        return comp_cset

    def complement(self):
        return [self.complement_set(self.sets[0]), self.complement_set(self.sets[1])]

    def containment(self):
        for element in self.sets[1]:
            chi_set1 = self.sets[0][element] if element in self.sets[0] else 0
            chi_set2 = self.sets[1][element]
            if not (chi_set1 <= chi_set2):
                return False
        return True

    
