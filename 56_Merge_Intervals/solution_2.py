class Solution:
    def merge(self, intervals: list) -> list:
        if not intervals:
            return intervals
        intervals.sort(key=lambda x: x[0])
        i = 1
        while i < len(intervals):
            if intervals[i][0] <= intervals[i-1][1]:
                intervals[i-1][1] = max(intervals[i-1][1], intervals[i][1])
                intervals.pop(i)
            else:
                i += 1
        return intervals


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        [[1, 3], [2, 6], [8, 10], [15, 18]],
        [[1, 4], [4, 5]],
    ]

    for intervals in test_cases:
        print(solution.merge(intervals))

