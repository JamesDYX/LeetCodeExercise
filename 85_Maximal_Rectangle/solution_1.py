class Solution:
    """based on largest rectangle in histogram"""
    def maximalRectangle(self, matrix: list) -> int:
        if not matrix or not matrix[0]:
            return 0
        res = 0
        heights = [0] * (len(matrix[0])+1)
        for row in matrix:
            index_stack = []
            for index in range(len(matrix[0])+1):
                heights[index] = heights[index] + 1 if index<len(matrix[0]) and row[index] == '1' \
                    else 0
                while index_stack and heights[index_stack[-1]] > heights[index]:
                    h = heights[index_stack.pop()]
                    start = index_stack[-1] + 1 if index_stack else 0
                    res = max(res, (index-start) * h)
                index_stack.append(index)
        return res


if __name__ == '__main__':
    test_case = [
      ["1","0","1","0","0"],
      ["1","0","1","1","1"],
      ["1","1","1","1","1"],
      ["1","0","0","1","0"]
    ]

    solution = Solution()
    print(solution.maximalRectangle(test_case))
