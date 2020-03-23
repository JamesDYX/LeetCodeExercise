class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        output = [""] * numRows
        line_id = 0
        acc_direction = 1
        for char in s:
            output[line_id] += char
            line_id += acc_direction
            if line_id == 0 or line_id == numRows-1:
                acc_direction *= -1
        return "".join(output)


if __name__ == '__main__':
    test_cases = [
        ("PAYPALISHIRING", 3),
        ("PAYPALISHIRING", 4),
    ]

    solution = Solution()
    for s, numRows in test_cases:
        print(solution.convert(s, numRows))