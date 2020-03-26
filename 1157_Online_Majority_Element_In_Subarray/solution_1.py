import numpy as np


class MajorityChecker:
    """
    use bincount in numpy
    """
    def __init__(self, arr: list):
        self.a = np.array(arr)

    def query(self, left, right, threshold):
        c = np.bincount(self.a[left:right+1])
        x = np.argmax(c)
        return x if c[x] >= threshold else -1