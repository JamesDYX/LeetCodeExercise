class Solution:
    def maxArea(self, height: list) -> int:
        left = 0
        right = len(height)-1

        max_area = 0
        while left != right:
            height_left = height[left]
            height_right = height[right]
            if height_left < height_right:
                max_area = max(max_area, height_left * (right - left))
                left += 1
            else:
                max_area = max(max_area, height_right * (right - left))
                right -= 1
        return max_area


if __name__ == '__main__':
    test_cases = [
        [1, 8, 6, 2, 5, 4, 8, 3, 7],
    ]

    solution = Solution()
    for height in test_cases:
        print(solution.maxArea(height))
