class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        if length < 2:
            return s

        max_length = 0
        from_index = 0
        to_index = 1
        for index in range(1, length):
            if index >= 2 and s[index] == s[index-2]:
                left_index, right_index = index-3, index+1

                while left_index >= 0 and right_index < length and s[left_index] == s[right_index]:
                    left_index -= 1
                    right_index += 1
                temp_length = right_index - left_index - 1
                if temp_length > max_length:
                    max_length = temp_length
                    from_index = left_index + 1
                    to_index = right_index

            if s[index] == s[index-1]:
                left_index, right_index = index - 2, index+1

                while left_index >= 0 and right_index < length and s[left_index] == s[right_index]:
                    left_index -= 1
                    right_index += 1
                temp_length = right_index - left_index - 1
                if temp_length > max_length:
                    max_length = temp_length
                    from_index = left_index + 1
                    to_index = right_index

        return s[from_index:to_index]


if __name__ == '__main__':
    test_cases = [
        "babad",
        "cbbd",
        "aaaa",
        "ccc",
        "ccd"
    ]

    solution = Solution()
    for s in test_cases:
        print(solution.longestPalindrome(s))