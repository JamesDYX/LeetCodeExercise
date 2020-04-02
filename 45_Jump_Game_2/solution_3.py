class Solution:
    """
    Greedy
    """
    def jump(self, nums: list) -> int:

        size = len(nums)

        destination = size - 1
        cur_coverage, last_jump_index = 0, 0
        times_of_jump = 0

        if size == 1:
            return 0

        for i in range(0, size-1):

            cur_coverage = max(cur_coverage, i + nums[i])

            if cur_coverage >= destination:
                return times_of_jump + 1

            # forced to jump (by lazy jump) to extend coverage
            if i == last_jump_index:

                last_jump_index = cur_coverage

                times_of_jump += 1

        return times_of_jump


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        [2, 3, 1, 1, 4],
        [9, 2]
    ]
    for nums in test_cases:
        print(solution.jump(nums))
