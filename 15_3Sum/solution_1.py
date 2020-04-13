class Solution:
    def threeSum(self, nums: list) -> list:
        hash_map = {}
        solutions = []
        for value in nums:
            if value not in hash_map:
                hash_map[value] = 1
            else:
                hash_map[value] += 1

        while hash_map:
            x, number_x = hash_map.popitem()
            if number_x > 1:
                hash_map[x] = number_x-1

            value = -x
            temp_hash = hash_map.copy()
            while temp_hash:
                y, number_y = temp_hash.popitem()
                z = value - y
                if z in temp_hash:
                    solutions.append([x, y, z])
                if y + y == value and number_y > 1:
                    solutions.append([x, y, y])

            if number_x > 1:
                hash_map.pop(x)

        return solutions


if __name__ == '__main__':
    test_cases = [
        [-1, 0, 1, 2, -1, -4],
        [-1, 0, 1, 2, -1, -4, 0, 0],
    ]

    solution = Solution()
    for nums in test_cases:
        print(solution.threeSum(nums))
