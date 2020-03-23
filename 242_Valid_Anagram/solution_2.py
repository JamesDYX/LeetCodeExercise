class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            length = len(s)
        else:
            return False

        counter = [0] * 26
        for index in range(length):
            char_1 = s[index]
            char_2 = t[index]
            if char_1 == char_2:
                continue
            counter[ord(char_1) - ord('a')] += 1
            counter[ord(char_2) - ord('a')] -= 1
        for value in counter:
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