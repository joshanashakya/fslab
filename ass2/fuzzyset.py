'''
Class to perform fuzzy set operations: union, intersection, complement, and containment.
'''

class FuzzySetOp:

    def __init__(self, domain, sets):
        self.domain = domain
        self.sets = sets

    def merge_sets(self):
        merged_set = {}
        for element in self.sets:
            merged_set.update(element)
        return merged_set.keys()

    def union(self):
        union = {}
        elements = self.merge_sets()
        for element in elements:
            mu_set1 = self.sets[0][element] if element in self.sets[0] else 0
            mu_set2 = self.sets[1][element] if element in self.sets[1] else 0
            mu_element = max(mu_set1, mu_set2)
            if mu_element != 0:
                union[element] = mu_element
        return union

    def intersection(self):
        intersection = {}
        elements = self.merge_sets()
        for element in elements:
            mu_set1 = self.sets[0][element] if element in self.sets[0] else 0
            mu_set2 = self.sets[1][element] if element in self.sets[1] else 0
            mu_element = min(mu_set1, mu_set2)
            if mu_element != 0:
                intersection[element] = mu_element
        return intersection

    def complement_set(self, fset):
        comp_fset = {}
        for element in self.domain:
            mu_fset = fset[element] if element in fset else 0
            mu_element = round((1-mu_fset), 1) if (1 - mu_fset) == 0.09999999999999998 else (1-mu_fset)
            if mu_element != 1:
                comp_fset[element] = mu_element
        return comp_fset

    def complement(self):
        return [self.complement_set(self.sets[0]), self.complement_set(self.sets[1])]

    def containment(self):
        for element in self.sets[0]:
            mu_set1 = self.sets[0][element]
            mu_set2 = self.sets[1][element] if element in self.sets[1] else 0
            if not (mu_set1 <= mu_set2):
                return False
        return True

    def alpha_cut(self, alpha, fset):
        alphacut_set = []
        for element in fset:
            if fset[element] >= alpha:
                alphacut_set.append(element)
        return alphacut_set

    def alphacut(self, alpha):
        return [self.alpha_cut(alpha, self.sets[0]), self.alpha_cut(alpha, self.sets[1])]


    