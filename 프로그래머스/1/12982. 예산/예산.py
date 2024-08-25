import numpy as np

def solution(d, budget):
    acc = np.add.accumulate(sorted(d))
    return(int(sum(acc <= budget)))