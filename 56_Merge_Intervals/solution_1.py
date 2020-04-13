class Solution:
    def merge(self, intervals: list) -> list:
        if not intervals:
            return intervals
        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]
        for interval in intervals:
            if interval[0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], interval[1])
            else:
                result.append(interval)
        return result


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        [[1, 3], [2, 6], [8, 10], [15, 18]],
        [[1, 4], [4, 5]],
    ]

    for intervals in test_cases:
        print(solution.merge(intervals))
