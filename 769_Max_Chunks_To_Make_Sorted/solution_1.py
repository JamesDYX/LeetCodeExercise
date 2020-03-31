class Solution:
    """
    binary search
    O(nlogn)
    """
    def maxChunksToSorted(self, arr: list) -> int:
        intervals = [[arr[0], arr[0]]]
        left_bound = right_bound = 0
        for value in arr[1:]:
            left, right = left_bound, right_bound
            while left <= right:
                mid = (left + right) // 2
                if value >= intervals[mid][1]:
                    left = mid + 1
                elif value < intervals[mid][0]:
                    right = mid - 1
                else:
                    left = mid
                    break
            if left == len(intervals):
                intervals.append([value, value])
            elif left > right_bound:
                intervals[left] = [value, value]
            else:
                intervals[left] = [min(value, intervals[left][0]), intervals[right_bound][1]]
            right_bound = left
        return right_bound - left_bound + 1


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        [4, 3, 2, 1, 0],
        [1, 0, 2, 3, 4],
        [1,2,3,4,5],
        [2,1,3, 0, 4],
        [1, 4, 0, 2, 3, 5],
        [0, 4, 7, 5, 3, 6, 9, 2, 1, 8]
    ]
    for arr in test_cases:
        print(solution.maxChunksToSorted(arr))
