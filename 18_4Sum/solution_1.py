class Solution:
    """
    use hash map
    """
    def fourSum(self, nums: list, target: int) -> list:
        nums1_dict = {}
        res = []
        for num in nums:
            if num in nums1_dict:
                nums1_dict[num] += 1
            else:
                nums1_dict[num] = 1
        for num1 in nums1_dict.keys():
            nums1_dict[num1] -= 1

            nums2_dict = nums1_dict.copy()
            for num2 in nums2_dict:
                if nums2_dict[num2] == 0:
                    continue
                nums2_dict[num2] -= 1

                nums3_dict = nums2_dict.copy()
                for num3 in nums3_dict.keys():
                    if nums3_dict[num3] == 0:
                        continue
                    nums3_dict[num3] -= 1
                    current_target = target - num1 - num2 - num3
                    if current_target in nums3_dict and nums3_dict[current_target] != 0:
                        nums3_dict[current_target] = 0
                        res.append([num1, num2, num3, current_target])
                    nums3_dict[num3] = 0
                nums2_dict[num2] = 0
            nums1_dict[num1] = 0
        return res


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        ([1, 0, -1, 0, -2, 2], 0),
        ([0, 0, 0, 0], 0)
    ]
    for nums, target in test_cases:
        print(solution.fourSum(nums, target))
