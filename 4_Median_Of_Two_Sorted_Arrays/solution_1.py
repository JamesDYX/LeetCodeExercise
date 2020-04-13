class Solution:
    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
        len_1 = len(nums1)
        len_2 = len(nums2)

        target_counter = int((len_1+len_2+1)/2)
        need_another = False
        if (len_1+len_2) % 2 == 0:
            need_another = True
        i, j = 0, 0
        median1 = None
        while i < len_1 and j < len_2:
            if nums1[i] <= nums2[j]:
                i += 1
                if i + j == target_counter:
                    median1 = nums1[i-1]
                    break
            else:
                j += 1
                if i + j == target_counter:
                    median1 = nums2[j-1]
                    break

        if median1 is None:
            if i == len_1:
                median1 = nums2[target_counter-len_1-1]
                if need_another:
                    median2 = nums2[target_counter-len_1]
                    return (median1 + median2) / 2
                else:
                    return median1
            else:
                median1 = nums1[target_counter-len_2-1]
                if need_another:
                    median2 = nums1[target_counter-len_2]
                    return (median1 + median2) / 2
                else:
                    return median1
        elif not need_another:
            return median1
        else:
            if i == len_1:
                median2 = nums2[j]
            elif j == len_2:
                median2 = nums1[i]
            elif nums1[i] > nums2[j]:
                median2 = nums2[j]
            else:
                median2 = nums1[i]
            return (median1 + median2) / 2


if __name__ == '__main__':
    test_cases = [
        ([1, 3], [2]),
        ([1, 2], [3, 4]),
        ([1, 2, 3], [4, 5, 6, 7, 8, 9, 10]),
    ]

    solution = Solution()
    for nums1, nums2 in test_cases:
        print(solution.findMedianSortedArrays(nums1, nums2))
