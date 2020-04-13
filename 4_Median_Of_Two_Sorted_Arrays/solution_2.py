class Solution:
    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        len1 = len(nums1)
        len2 = len(nums2)
        half_size = int((len1+len2+1)/2)
        need_another = False
        if (len1 + len2) % 2 == 0:
            need_another = True

        if len1 == 0:
            median1 = nums2[half_size-1]
            if need_another:
                median2 = nums2[half_size]
                return (median1 + median2) / 2
            return median1

        partition1 = int((len1+1)/2)
        partition2 = half_size-partition1
        while True:
            if partition1 > 0 and nums1[partition1-1] > nums2[partition2]:
                partition1 -= 1
                partition2 += 1
            elif partition1 < len1 and nums2[partition2-1] > nums1[partition1]:
                partition1 += 1
                partition2 -= 1
            else:
                break

        if partition1 <= 0:
            median1 = nums2[partition2-1]
        elif partition2 <= 0:
            median1 = nums1[partition1-1]
        elif nums1[partition1-1] <= nums2[partition2-1]:
            median1 = nums2[partition2 - 1]
        else:
            median1 = nums1[partition1-1]
        if not need_another:
            return median1

        if partition1 >= len1:
            median2 = nums2[partition2]
        elif partition2 >= len2:
            median2 = nums1[partition1]
        elif nums1[partition1] >= nums2[partition2]:
            median2 = nums2[partition2]
        else:
            median2 = nums1[partition1]

        median = (median1 + median2) / 2
        return median


if __name__ == '__main__':
    test_cases = [
        ([3], [-2, -1]),
        ([], [1]),
        ([1, 3], [2]),
        ([1, 2], [3, 4]),
        ([1, 2, 3], [4, 5, 6, 7, 8, 9, 10]),
        ([4, 5, 6, 7, 8, 9, 10], [1, 2, 3]),
    ]

    solution = Solution()
    for nums1, nums2 in test_cases:
        print(solution.findMedianSortedArrays(nums1, nums2))