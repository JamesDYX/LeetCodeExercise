import numpy as np


class ProductOfNumbers:
    """
    Prefix Product Array
    """
    def __init__(self):
        self.product = np.array([], dtype=int)

    def add(self, num: int) -> None:
        self.product *= num
        self.product = np.append(self.product, num)

    def getProduct(self, k: int) -> int:
        return self.product[-k]


if __name__ == '__main__':
    productOfNumbers = ProductOfNumbers()
    productOfNumbers.add(3)
    print(productOfNumbers.getProduct(1))
    productOfNumbers.add(0)
    productOfNumbers.add(2)
    productOfNumbers.add(5)
    productOfNumbers.add(4)
    print(productOfNumbers.getProduct(2))
    print(productOfNumbers.getProduct(3))
    print(productOfNumbers.getProduct(4))
    productOfNumbers.add(8)
    print(productOfNumbers.getProduct(2))
