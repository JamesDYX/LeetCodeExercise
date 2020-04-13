class RLEIterator:
    """
    Binary Search
    """
    def __init__(self, A: list):
        self.A = []
        i = 0
        while i < len(A):
            if not A[i]:
                i += 2
                continue
            if not self.A:
                self.A.append([A[i], A[i+1]])
            else:
                self.A.append([A[i]+self.A[-1][0], A[i+1]])
            i += 2
        self.passed = 0
        self.left_bound = 0
        self.right_bound = len(self.A) - 1
        self.end = False

    def next(self, n: int) -> int:
        if self.end:
            return -1
        self.passed += n
        left = self.left_bound
        right = self.right_bound
        while left <= right:
            mid = (left + right) // 2
            if self.A[mid][0] == self.passed:
                left = mid
                break
            elif self.A[mid][0] < self.passed:
                left = mid + 1
            else:
                right = mid - 1
        if left > self.right_bound:
            self.end = True
            return -1
        elif self.A[left][0] == self.passed:
            self.left_bound = left + 1
        else:
            self.left_bound = left
        return self.A[left][1]


if __name__ == '__main__':
    a = RLEIterator([3,8,0,9,2,5])
    print(a.next(2))
    print(a.next(1))
    print(a.next(1))
    print(a.next(2))
    print(a.next(10))
