import time
import random
import numpy as np
import matplotlib.pyplot as plt
from hw5.bayes_net import BayesNet
from hw5.utils import Node


def CSRW_BN():
    C = Node("C", [], [0.5])
    S = Node("S", [C], [0.1,0.5])
    R = Node("R", [C], [0.8,0.2])
    W = Node("W", [S,R], [0.99,0.9,0.9,0])
    return BayesNet([C,S,R,W])

def random_BN(numNodes, maxParents):
    nodes = []
    for n in range(numNodes):
        numParents = random.randint(0, min(maxParents,len(nodes)))
        parents = random.sample(nodes, k=numParents)
        CPT = np.random.random(size=2**numParents)
        nodes.append(Node(str(n), parents, CPT))
    return BayesNet(nodes)


def main():
    bn = random_BN(20,5)
    n = random.sample(bn.nodes, k=6)
    evidence = dict(zip(n[:5], np.random.randint(0,2,10)))
    node = n[-1]

    # TODO: 4.4, 4.5

if __name__ == "__main__":
    main()