class Solution:
    def countBits(self, num: int) -> list:
        res = [0]
        shift = 1
        counter = 0
        for i in range(1, num+1):
            res.append(res[i-shift] + 1)
            counter += 1
            if counter == shift:
                shift *= 2
                counter = 0
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.countBits(0))
