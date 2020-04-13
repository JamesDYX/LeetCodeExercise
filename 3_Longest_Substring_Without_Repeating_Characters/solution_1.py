class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = ''
        max_length = 0
        for c in s:
            index = substring.find(c)
            substring += c
            if index == -1:
                max_length = max(max_length, len(substring))
            else:
                substring = substring[index+1:]
        return max_length


if __name__ == '__main__':
    test_cases = [
        "abcabcbb",
        "bbbbb",
        "pwwkew",
        "dvdf",
    ]

    solution = Solution()
    for s in test_cases:
        print(solution.lengthOfLongestSubstring(s))
