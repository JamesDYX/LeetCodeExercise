class Solution:
    """
    python solution of
    https://leetcode.com/problems/task-scheduler/discuss/104496/concise-Java-Solution-O(N)-time-O(26)-space
    """
    def leastInterval(self, tasks: list, n: int) -> int:
        counter = [0 for i in range(26)]
        for ch in tasks:
            counter[ord(ch) - ord('A')] += 1
        counter.sort(reverse=True)
        i = 1
        while i < 26 and counter[i] == counter[0]:
            i += 1
        return max(len(tasks), (counter[0] - 1) * (n + 1) + i)


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        (["A", "A", "A", "B", "B", "B"], 2)
    ]
    for tasks, n in test_cases:
        print(solution.leastInterval(tasks, n))
