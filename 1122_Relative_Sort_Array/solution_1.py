class Solution:
    def relativeSortArray(self, arr1: list, arr2: list) -> list:
        res_dic = {}
        remain = []
        for num in arr2:
            res_dic[num] = 0
        for num in arr1:
            if num in res_dic:
                res_dic[num] += 1
            else:
                remain.append(num)
        remain.sort()
        res = []
        for key, value in res_dic.items():
            res += [key] * value
        return res + remain


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        ([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]),
    ]
    for arr1, arr2 in test_cases:
        print(solution.relativeSortArray(arr1, arr2))
