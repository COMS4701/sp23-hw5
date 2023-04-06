import numpy as np
from hw5.utils import Node


class BayesNet:
    def __init__(self, nodes=[]):
        self.nodes = nodes
        self.topological_sort()
        self.set_children()
    
    def topological_sort(self):
        new = []
        while self.nodes:
            for n in self.nodes:
                if set(n.parents) <= set(new):
                    new.append(n)
                    self.nodes.remove(n)
        self.nodes = new

    def set_children(self):
        for n in self.nodes:
            for p in n.parents:
                p.children.add(n)


    """
    4.1 Generate sample and weight from Bayes net by likelihood weighting
    """        
    def weighted_sample(self, evidence: dict={}):
        """
        Args:
            evidence (Dict): {Node:0/1} mappings for evidence nodes.
        Returns:
            Dict: {Node:0/1} mappings for all nodes.
            Float: Sample weight. 
        """
        sample = {}
        weight = 1
        # TODO: 4.1
        return sample, weight

    """
    4.2 Generate sample from Bayes net by Gibbs sampling
    """  
    def gibbs_sample(self, node: Node, sample: dict):
        """
        Args:
            node (Node): Node to resample.
            sample (Dict): {node:0/1} mappings for all nodes.
        Returns:
            Dict: {Node:0/1} mappings for all nodes.
        """ 
        new = sample.copy()
        # TODO: 4.2       
        return new

    """
    4.3 Generate a list of samples given evidence and estimate the distribution.
    """  
    def gen_samples(self, numSamples: int, evidence: dict={}, LW: bool=True):
        """
        Args:
            numSamples (int).
            evidence (Dict): {Node:0/1} mappings for evidence nodes.
            LW (bool): Use likelihood weighting if True, Gibbs sampling if False.
        Returns:
            List[Dict]: List of {node:0/1} mappings for all nodes.
            List[float]: List of corresponding weights.
        """       
        # TODO: 4.3
        return [], []

    def estimate_dist(self, node: Node, samples: list[dict], weights: list[float]):
        """
        Args:
            node (Node): Node whose distribution we will estimate.
            samples (List[Dict]): List of {node:0/1} mappings for all nodes.
            weights (List[float]: List of corresponding weights.
        Returns:
            Tuple(float, float): Estimated distribution of node variable.
        """           
        # TODO: 4.3
        return (0,0)
