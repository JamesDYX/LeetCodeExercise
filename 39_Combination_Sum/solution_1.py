class Solution:
    def combinationSum(self, candidates: list, target: int):
        solution_dic = {}

        def dp(start_index, current_target):
            if (start_index, current_target) in solution_dic:
                return solution_dic[(start_index, current_target)]

            solutions = []
            i = 1
            while True:
                new_target = current_target - candidates[start_index] * i
                if new_target < 0:
                    break
                elif new_target == 0:
                    solutions.append([candidates[start_index]] * i)
                    break
                else:
                    prefix_solution = [candidates[start_index]] * i
                    for new_index in range(start_index+1, len(candidates)):
                        temp_solutions = dp(new_index, new_target)
                        if not temp_solutions:
                            continue
                        solutions += [prefix_solution + temp_solution for temp_solution in temp_solutions]
                i += 1
            solution_dic[(start_index, current_target)] = solutions
            return solutions

        res = []
        for index in range(len(candidates)):
            res += dp(index, target)
        return res


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        ([2,3,6,7], 7),
        ([2,3,5], 8)
    ]
    for candidates, target in test_cases:
        print(solution.combinationSum(candidates, target))
