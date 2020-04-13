class Solution:
    """
    The code simulates the process of revealing

    however, manually we can get a answer in this way:

    for input [1, 2, 3, 4, 5, 6, 7, 8 ,9 ,10, 11, 12], resort the list like this

    ^    1    2    3    4    5    6      len0 = (length + 1) // 2
    ^        7       8       9           len1 = (length - len0 + 1) // 2
    ^            10      11              len2 = (length - len0 - len1 + 1) // 2
    |                12                  len3 = (length - len0 - len1 - len2 + 1) // 2

        Then from the bottom layer to the top layer,
        layer by layer, insert the lower layer to upper layer's interval, and get
        [12]
        [10, 12, 11]
        [7, 10, 8, 12, 9, 11]
        [1, 7, 2, 10, 3, 8, 4, 12, 5, 9, 6, 11]  <-- answer

    """

    def deckRevealedIncreasing(self, deck: list) -> list:
        deck = sorted(deck)
        reveal_index_simulator = list(range(len(deck)))
        answer = [0] * len(deck)
        for card in deck:
            reveal_index = reveal_index_simulator.pop(0)
            answer[reveal_index] = card
            if reveal_index_simulator:
                reveal_index_simulator.append(reveal_index_simulator.pop(0))
        return answer


if __name__ == '__main__':
    test_case = [1, 2, 3, 4, 5, 6, 7, 8 ,9 ,10, 11, 12]
    solution = Solution()
    print(solution.deckRevealedIncreasing(test_case))
