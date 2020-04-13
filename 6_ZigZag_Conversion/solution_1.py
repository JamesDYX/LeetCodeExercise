class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        interval = (numRows-1) * 2
        max_length = len(s)
        result = ""

        # the first row
        for index in range(0, max_length, interval):
            result += s[index]

        for row_id in range(1, numRows-1):
            index = row_id
            intervals = [interval-row_id*2, row_id*2]
            pointer = 0
            while index < max_length:
                result += s[index]
                index += intervals[pointer]
                pointer = 1 - pointer
        # the last row:
        for index in range(numRows-1, max_length, interval):
            result += s[index]

        return result


if __name__ == '__main__':
    test_cases = [
        ("PAYPALISHIRING", 3),
        ("PAYPALISHIRING", 4),
    ]

    solution = Solution()
    for s, numRows in test_cases:
        print(solution.convert(s, numRows))
