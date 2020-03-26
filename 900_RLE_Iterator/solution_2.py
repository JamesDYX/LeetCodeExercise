class RLEIterator:
    """
    Recursive
    """
    def __init__(self, A: list):
        self.A = A
        self.current = 0

    def next(self, n: int) -> int:
        # If we have exhausted all numbers in the sequence, return -1
        if self.current == len(self.A):
            return -1

        # Check if we are going to exhaust all of the current number we are looking at.
        if self.A[self.current] < n:
            n -= self.A[self.current]  # Decrement n by the amount of the current number.
            self.current += 2  # Look at the next number.
            return self.next(n)  # Return the next n in the sequence.

        # If we are not going to exhaust all of the current number,
        # decrement the amount exhausted by n and return the number.
        self.A[self.current] -= n
        return self.A[self.current + 1]