from random import choice


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.dic:
            return False
        self.dic[val] = val
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.dic:
            return False
        del self.dic[val]
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return choice(list(self.dic.keys()))


if __name__ == '__main__':
    solution = RandomizedSet()
    print(solution.insert(1))
    print(solution.remove(2))
    print(solution.insert(2))
    print(solution.getRandom())
