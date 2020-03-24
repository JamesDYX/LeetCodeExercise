class Solution:
    """
    binary search
    min capacity = max(max(weights), avg(weights))
    max capacity = sum(weights)
    search range = [min_capacity, max_capacity]
    """
    def shipWithinDays(self, weights: list, D: int) -> int:
        max_capacity = sum(weights)
        avg_capacity = max_capacity // len(weights)
        min_capacity = max(max(weights), avg_capacity)
        while min_capacity < max_capacity:
            capacity = (min_capacity + max_capacity) // 2
            need_day = 1
            have_load = 0
            for weight in weights:
                have_load += weight
                if have_load > capacity:
                    have_load = weight
                    need_day += 1
                    if need_day > D:
                        break
            if need_day > D:
                min_capacity = capacity+1
            else:
                max_capacity = capacity
        return min_capacity


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        ([1,2,3,4,5,6,7,8,9,10], 5),
        ([3,2,2,4,1,4],3),
        ([1,2,3,1,1], 4)
    ]

    for weights, D in test_cases:
        print(solution.shipWithinDays(weights, D))
