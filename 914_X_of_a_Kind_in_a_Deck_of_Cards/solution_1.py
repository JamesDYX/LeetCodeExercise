class Solution:
    def hasGroupsSizeX(self, deck: list) -> bool:
        hash_table = {}
        length = len(deck)
        if length < 2:
            return False
        for card in deck:
            if card in hash_table:
                hash_table[card] += 1
            else:
                hash_table[card] = 1

        for i in range(2, 1 + min(hash_table.values())):
            if length % i != 0:
                continue
            success = True
            for value in hash_table.values():
                if value % i != 0:
                    success = False
                    break
            if success:
                return True

        return False


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        [1, 2, 3, 4, 4, 3, 2, 1],
        [1, 1, 1, 2, 2, 2, 3, 3],
        [1],
        [1, 1],
        [1, 1, 2, 2, 2, 2],
        [1,1,1,1,1,1,1,2,2,2,2,2,2,2,3,3,3,3,3,3,3]
    ]

    for test_case in test_cases:
        print(solution.hasGroupsSizeX(test_case))
