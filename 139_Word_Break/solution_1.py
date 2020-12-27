class Solution:
    def wordBreak(self, s: str, wordDict: list) -> bool:
        wordDict = set(wordDict)
        res_list = [True]
        for i in range(len(s)):
            can_break = False
            for j in range(i, -1, -1):
                can_break = s[j: i+1] in wordDict and res_list[j]
                if can_break:
                    break
            res_list.append(can_break)

        return res_list[-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.wordBreak("", ["apple", "pen"]))
