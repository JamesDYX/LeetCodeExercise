class Solution:
    def combinationSum2(self, candidates: list, target: int):
        self.solution_dict = {}
        self.candidates = [0] + candidates
        self.candidates.sort()
        res = self.dp(0, target)
        return [temp[1:] for temp in res]

    def dp(self, start_index, current_target):
        if (start_index, current_target) in self.solution_dict:
            return self.solution_dict[(start_index, current_target)]
        else:
            solution_set = []
            new_index = start_index+1
            while new_index < len(self.candidates) and self.candidates[new_index] == self.candidates[start_index]:
                new_index += 1
            index_mem = new_index
            for i in range(new_index-start_index):
                solution = [self.candidates[start_index]] * (i+1)
                new_target = current_target - self.candidates[start_index] * (i+1)
                if new_target == 0:
                    solution_set.append(solution)
                    break
                elif new_target < 0:
                    break
                last_num = self.candidates[start_index]
                while new_index < len(self.candidates):
                    if self.candidates[new_index] == last_num:
                        new_index += 1
                        continue
                    last_num = self.candidates[new_index]
                    new_set = self.dp(new_index, new_target)
                    if new_set:
                        solution_set += [(solution + new_solution) for new_solution in new_set]
                    new_index += 1
                new_index = index_mem
            self.solution_dict[(start_index, current_target)] = solution_set
            return solution_set


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        ([10,1,2,7,6,1,5], 8),
        ([2,5,2,1,2], 5)
    ]
    for nums, tar in test_cases:
        print(solution.combinationSum2(nums, tar))
