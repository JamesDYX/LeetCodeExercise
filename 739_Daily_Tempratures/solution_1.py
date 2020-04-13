class Solution:
    def dailyTemperatures(self, T: list) -> list:
        result = [0] * len(T)
        index_stack = []
        for index in range(len(T)):
            while index_stack and T[index] > T[index_stack[-1]]:
                start_index = index_stack.pop()
                result[start_index] = index - start_index
            index_stack.append(index)
        return result


if __name__ == '__main__':
    test_cases = [
        [73, 74, 75, 71, 69, 72, 76, 73],
    ]

    solution = Solution()
    for temprature in test_cases:
        print(solution.dailyTemperatures(temprature))
