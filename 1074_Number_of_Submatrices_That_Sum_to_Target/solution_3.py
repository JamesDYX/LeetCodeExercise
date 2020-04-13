import numpy


class Solution:
    """
    https://www.acwing.com/solution/leetcode/content/2366/
    O(n^3), however TLE
    """
    def numSubmatrixSumTarget(self, matrix: list, target: int) -> int:
        matrix = numpy.array(matrix)
        res = 0
        size_1 = len(matrix[0])
        size_2 = len(matrix)
        for i in range(size_1):
            for i_ in range(i, size_1):
                sub_prefix = matrix[:, i:i_+1].sum(1)
                prefix_hash = {0: 1}
                for j in range(size_2):
                    prefix_sum = sub_prefix[0:j+1].sum()
                    sub_target = prefix_sum - target
                    if sub_target in prefix_hash:
                        res += prefix_hash[sub_target]
                    if prefix_sum in prefix_hash:
                        prefix_hash[prefix_sum] += 1
                    else:
                        prefix_hash[prefix_sum] = 1
        return res


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        ([[0,1,0],[1,1,1],[0,1,0]], 0),
        ([[1,-1],[-1,1]], 0)
    ]

    for mat, target in test_cases:
        print(solution.numSubmatrixSumTarget(mat, target))
