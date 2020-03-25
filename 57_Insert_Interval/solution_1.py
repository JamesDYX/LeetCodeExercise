class Solution:
    def insert(self, intervals: list, newInterval: list) -> list:
        def bin_search(point, left, right):
            l, r = left, right
            while l <= r:
                mid = (l + r) // 2
                if intervals[mid][0] <= point <= intervals[mid][1]:
                    return mid, True
                elif intervals[mid][0] > point:
                    r = mid-1
                else:
                    l = mid + 1
            return l, False

        l_index, l_find = bin_search(newInterval[0], 0, len(intervals)-1)
        r_index, r_find = bin_search(newInterval[1], l_index, len(intervals)-1)
        if l_find and r_find:
            intervals[l_index][1] = intervals[r_index][1]
            return intervals[:l_index+1] + intervals[r_index+1:]
        elif (not l_find) and r_find:
            intervals[l_index][1] = intervals[r_index][1]
            intervals[l_index][0] = newInterval[0]
            return intervals[:l_index + 1] + intervals[r_index + 1:]
        elif l_find and (not r_find):
            intervals[l_index][1] = newInterval[1]
            return intervals[:l_index + 1] + intervals[r_index:]
        else:
            return intervals[:l_index] + [newInterval] + intervals[r_index:]


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
            # ([[1,3],[6,9]], [2,5]),
            # ([[1,2],[3,5],[6,7],[8,10],[12,16]], [4, 8]),
            # ([[1, 2], [4, 5], [6, 7], [8, 10], [12, 16]], [3, 8]),
            # ([[1, 2], [4, 5], [6, 7], [8, 10], [12, 16]], [3, 11]),
            # ([[1, 2], [4, 5], [6, 7], [8, 10], [12, 16]], [3, 3]),
        ([], [1,2])
    ]

    for intervals, newInterval in test_cases:
        print(solution.insert(intervals, newInterval))
