from bisect import bisect


class Solution:
    def numSmallerByFrequency(self, queries: list, words: list) -> list:
        f_words = []

        for string in words:
            f_words.append(string.count(min(string)))

        f_words.sort()
        res = []

        for string in queries:
            f_string = string.count(min(string))
            id = bisect(f_words, f_string)
            res.append(len(f_words) - id)

        return res

