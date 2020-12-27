class solution:

    def find_pivot(self, array: list):
        self.array = array
        left_min = array[0]

        left_index = 1
        right_index = len(array) - 1

        self.pivot_index = 0
        while left_index <= right_index:
            mid = (left_index + right_index) // 2
            if self.array[mid] > left_min:
                left_index = mid + 1
            else:
                self.pivot_index = mid
                right_index = mid - 1

    def binary_search(self, target):
        if self.array[0] <= target:
            left_index = 0
            right_index = self.pivot_index - 1
        else:
            left_index = self.pivot_index
            right_index = len(self.array) - 1

        while left_index <= right_index:
            mid = (left_index + right_index) // 2
            if self.array[mid] > target:
                right_index = mid - 1
            elif self.array[mid] == target:
                return mid
            else:
                left_index = mid + 1
        return -1

    def solve(self, array, target):
        self.find_pivot(array)
        return self.binary_search(target)
