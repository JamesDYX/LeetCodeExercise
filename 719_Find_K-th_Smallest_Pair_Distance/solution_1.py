class Solution:
    def smallestDistancePair(self, nums: list, k: int) -> int:
        nums.sort()
        left_bound = 0
        right_bound = nums[-1] - nums[0]
        res = 0
        # binary search
        while left_bound <= right_bound:
            mid = (left_bound + right_bound) // 2

            counter = 0
            found = False
            left_index = 1
            right_index = len(nums) - 1

            # counting the total pairs whose distance less than mid
            # use a sliding window
            while left_index <= right_index:
                mid_index = (left_index + right_index) // 2
                if nums[mid_index] == nums[0] + mid:
                    found = True
                    right_index = mid_index - 1
                elif nums[mid_index] > nums[0] + mid:
                    right_index = mid_index - 1
                else:
                    left_index = mid_index + 1

            left_index, right_index = 0, left_index
            counter += right_index - 1
            if counter > k - 1:
                right_bound = mid - 1
                continue
            while True:
                left_index += 1
                if right_index <= left_index:
                    right_index = left_index + 1
                while right_index < len(nums) and nums[right_index] - nums[left_index] < mid:
                    right_index += 1
                if right_index == len(nums):
                    counter += (len(nums) - left_index) * (len(nums) - left_index - 1) / 2
                    break
                else:
                    counter += right_index - left_index - 1
                    if nums[right_index] - nums[left_index] == mid:
                        found = True
                    if counter > k - 1:
                        break

            # adjust binary search
            if counter > k - 1:
                right_bound = mid - 1
            elif counter < k - 1:
                left_bound = mid + 1
                res = mid
            else:
                if found:
                    return mid
                else:
                    left_bound = mid + 1
        return res


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        ([1,3,1], 2)
    ]
    for nums, k in test_cases:
        print(solution.smallestDistancePair(nums, k))
