class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            length = len(s)
        else:
            return False

        counter = {}
        for index in range(length):
            char_1 = s[index]
            char_2 = t[index]

            if char_1 == char_2:
                continue
            if char_1 in counter:
                counter[char_1] += 1
            else:
                counter[char_1] = 1
            if char_2 in counter:
                counter[char_2] -= 1
            else:
                counter[char_2] = -1
        for value in counter.values():
            if value:
                return False
        return True


if __name__ == '__main__':
    test_cases = [
        ("anagram", "nagaram"),
        ("rat", "car"),
    ]

    solution = Solution()
    for s, t in test_cases:
        print(solution.isAnagram(s, t))
