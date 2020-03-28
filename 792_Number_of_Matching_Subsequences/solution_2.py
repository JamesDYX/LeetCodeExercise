import collections


class Solution:
    """
    This is a solution that idea is same to solution 1,
    but with a different and much quicker implementation
    """
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        ans = 0

        headers = collections.defaultdict(list)
        for word_idx in range(len(words)):
            headers[words[word_idx][0]].append((word_idx, 1))

        for letter in S:
            if letter in headers:
                stack = headers[letter]
                headers[letter] = []
                while stack:
                    word_idx, next_letter_idx = stack.pop()
                    if next_letter_idx == len(words[word_idx]):
                        ans += 1
                    else:
                        headers[words[word_idx][next_letter_idx]].append((word_idx, next_letter_idx + 1))

        return ans