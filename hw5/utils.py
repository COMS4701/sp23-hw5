import numpy as np


class Node:
    def __init__(self, name, parents, CPT):
        assert len(CPT) == 2**len(parents), "CPT incorrect size"
        self.name = name
        self.parents = parents
        self.CPT = CPT
        self.children = set()

    def get_probs(self, evidence=[]):
        """
        Returns (P(node=0|evidence), P(node=1|evidence)).
        Error if number of evidence values not equal to number of parents
        """
        assert len(evidence) == len(self.parents), "evidence incorrect size"
        idx = sum(val*(2**idx) for idx,val in enumerate(reversed(evidence)))
        return (self.CPT[idx], 1-self.CPT[idx])

    def sample(self, evidence=[]):
        """
        Returns 0 or 1 sampled using probability given evidence.
        """
        return np.random.choice([0,1], p=self.get_probs(evidence))
