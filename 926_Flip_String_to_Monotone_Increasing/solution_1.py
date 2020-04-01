class Solution:
    """
    Prefix Sum
    """
    def minFlipsMonoIncr(self, S: str) -> int:
        if S == "":
            return 0
        prefix_sum = []
        sum = 0
        for c in S:
            sum += int(c)
            prefix_sum.append(sum)
        length = len(S)
        res = min(length - prefix_sum[-1], prefix_sum[-1])
        if res == 0:
            return 0
        for index in range(1, length):
            if S[index] == '0':
                continue
            temp = prefix_sum[index-1] + length - index - (prefix_sum[-1] - prefix_sum[index-1])
            res = min(res, temp)
            if res == 0:
                return 0
        return res


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        "00110",
        "010110",
        "00011000",
        "",
        "11111",
        "00000"
    ]

    for S in test_cases:
        print(solution.minFlipsMonoIncr(S))
