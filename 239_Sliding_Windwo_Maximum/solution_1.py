class Solution:
    def maxSlidingWindow(self, nums: list, k: int) -> list:
        if k <= 1:
            return nums
        iter_num = len(nums)-k+1
        result = []
        start_pt = 0
        max_index = 0
        for i in range(1, k):
            if nums[i] >= nums[max_index]:
                max_index = i
        result.append(nums[max_index])
        for i in range(iter_num-1):
            start_pt += 1
            max_index -= 1
            if nums[start_pt+k-1] >= nums[start_pt+max_index]:
                max_index = k-1
            elif max_index < 0:
                max_index = 0
                for i in range(1, k):
                    if nums[start_pt+i] >= nums[start_pt+max_index]:
                        max_index = i
            result.append(nums[start_pt+max_index])
        return result


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        ([8, 3, -1, -3, 5, 3, 6, 7], 3)
    ]

    for test_case, k in test_cases:
        print(solution.maxSlidingWindow(test_case, k))