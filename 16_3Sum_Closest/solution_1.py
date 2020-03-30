import math


class Solution:
    def threeSumClosest(self, nums: list, target: int) -> int:
        nums.sort()
        length = len(nums)
        min_interval = math.inf
        res = 0
        for i in range(length-2):
            current_start = nums[i]
            if i != 0 and current_start == last_start:
                continue
            current_target = target - current_start
            left = i + 1
            right = length - 1

            while left < right:
                nums_1 = nums[left]
                nums_2 = nums[right]
                if nums_1 + nums_2 < current_target:
                    temp = current_start + nums_1 + nums_2
                    interval = abs(target - temp)
                    if interval < min_interval:
                        min_interval = interval
                        res = temp
                    left += 1
                elif nums_1 + nums_2 > current_target:
                    temp = current_start + nums_1 + nums_2
                    interval = abs(target - temp)
                    if interval < min_interval:
                        min_interval = interval
                        res = temp
                    right -= 1
                else:
                    return target
            last_start = current_start

        return res


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        ([-1, 2, 1, -4], 1),
        ([-1, 2, 1, -4], 2),
        ([1,2,5,10,11], 12)
    ]

    for nums, target in test_cases:
        print(solution.threeSumClosest(nums, target))
