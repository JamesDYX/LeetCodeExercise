class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        min_possible_length = 0
        p_index = 0
        p_len = len(p)
        while p_index < p_len:
            if p_index == p_len-1 or p[p_index+1] != '*':
                min_possible_length += 1
                p_index += 1
            else:
                p_index += 2

        return self._isMatch(s, p, min_possible_length)

    def _isMatch(self, s: str, p: str, min_possible_length: int) -> bool:
        length = len(s)
        if length < min_possible_length:
            return False
        if s == "" and min_possible_length == 0:
            return True
        _min_possible_length = min_possible_length
        p_index = 0
        s_index = 0
        p_len = len(p)
        while p_index < p_len:
            if p_index == p_len-1 or p[p_index+1] != '*':
                if s[s_index] != p[p_index] and p[p_index] != '.':
                    return False
                p_index += 1
                s_index += 1
                _min_possible_length -= 1
            else:
                break
        if p_index == p_len:
            if s_index == length:
                return True
            return False

        while True:
            if length - s_index < _min_possible_length:
                return False
            if self._isMatch(s[s_index:], p[p_index+2:], _min_possible_length):
                return True
            if p[p_index] == '.' or s[s_index] == p[p_index]:
                s_index += 1
            else:
                return False


if __name__ == '__main__':
    test_cases = [
        ("aaa", "ab*a"),
        ("aa", "a"),
        ("aa", "a*"),
        ("ab", ".*"),
        ("aab", "c*a*b"),
        ("mississippi", "mis*is*p*."),
        ("", ""),
        ("", "c*a*b*.*"),
        ("aa", "a*a"),
        ("aa", ".*a*a"),
        ("ab", ".*c"),
    ]

    solution = Solution()
    for s, p in test_cases:
        print(solution.isMatch(s, p))
