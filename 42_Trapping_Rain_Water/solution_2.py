class Solution:
    """
    similar to the idea of 11 Container with most water
    use two pointer
    """
    def trap(self, height: list) -> int:
        # remove redundant heights
        left = 0
        while left + 1 < len(height):
            if height[left+1] < height[left]:
                break
            left += 1
        right = len(height) - 1
        while right > left:
            if height[right-1] < height[right]:
                break
            right -= 1
        height = height[left:right+1]
        if not height:
            return 0

        # two pointer started
        sum = 0
        left = 0
        right = len(height) - 1
        water_height_l, water_height_r = height[0], height[-1]
        while left <= right:
            height_left, height_right = height[left], height[right]
            if height_left <= height_right:
                if height_left < water_height_l:
                    sum += water_height_l - height_left
                else:
                    water_height_l = height_left
                left += 1
            else:
                if height_right < water_height_r:
                    sum += water_height_r - height_right
                else:
                    water_height_r = height_right
                right -= 1

        return sum


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],
    ]

    for heights in test_cases:
        print(solution.trap(heights))
