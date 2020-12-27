class Solution:
    def numDecodings(self, s: str) -> int:
        first = 1
        second = 0

        last_char = ''
        for ch in s:
            if ch == '0':
                if last_char != '1' and last_char != '2':
                    return 0
                else:
                    first, second = second, first
            elif last_char + ch >= '27' or last_char == '0':
                first, second = first, first
            else:
                first, second = first + second, first
            last_char = ch
        return first


if __name__ == '__main__':
    solution = Solution()
    print(solution.numDecodings("101"))
