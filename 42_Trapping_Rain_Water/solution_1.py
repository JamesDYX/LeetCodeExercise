class Solution:
    """
    similar to the idea of 739 daily temperature
    use stack
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

        sum = 0
        index_stack = [0]
        for index in range(1, len(height)):
            value = height[index]
            while index_stack and value > height[index_stack[-1]]:
                left_index = index_stack.pop()
            if not index_stack:
                # when stack is empty,
                # means the left side should be the last index we just popped out
                # and the right side should be current index
                water_height = height[left_index]
                for i in range(left_index+1, index):
                    sum += water_height - height[i]
            index_stack.append(index)

        # fill the water between the rest indices in the stack
        right_i = 1
        while right_i < len(index_stack):
            right_index = index_stack[right_i]
            left_index = index_stack[right_i-1]
            water_height = height[right_index]
            for i in range(left_index + 1, right_index):
                sum += water_height - height[i]
            right_i += 1

        return sum


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],
    ]

    for heights in test_cases:
        print(solution.trap(heights))
