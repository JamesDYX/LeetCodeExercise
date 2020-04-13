class Solution:
    def numMatchingSubseq(self, S: str, words: list) -> int:
        res = 0
        dictionaries = [sorted(words)]
        for c in S:
            new_dictionaries = []
            for dictionary in dictionaries:
                # find the range of c in this dictionary
                left, right = 0, len(dictionary)-1
                possible_left, possible_right = None, len(dictionary)-1
                while left <= right:
                    mid = (left + right) // 2
                    if dictionary[mid][0] < c:
                        left = mid + 1
                    elif dictionary[mid][0] > c:
                        right = mid - 1
                        possible_right = right
                    else:
                        right = mid - 1
                        possible_left = mid if possible_left is None else possible_left

                # if not find c in current dictionary, means ths dictionary is not used by c
                # keep the dictionary unchanged
                if possible_left is None:
                    new_dictionaries.append(dictionary)
                    continue
                while possible_left <= possible_right:
                    mid = (possible_left + possible_right) // 2
                    if dictionary[mid][0] <= c:
                        possible_left = mid + 1
                    else:
                        possible_right = mid - 1

                # split the dictionary into two parts
                # part1: words that do not start with c
                # part2: words that start with c

                # for part1, add it to the dictionary list if it is not None
                temp_dict = dictionary[:left] + dictionary[possible_left:]
                if temp_dict:
                    new_dictionaries.append(temp_dict)

                # for part2, remove all words' first character
                # if the new word is None, means find a word which match the string
                # add the new part2 to the dictionary list
                temp_dict = dictionary[left:possible_left]
                new_temp_dict = []
                for word in temp_dict:
                    new_word = word[1:]
                    if new_word:
                        new_temp_dict.append(new_word)
                    else:
                        res += 1
                if new_temp_dict:
                    new_dictionaries.append(new_temp_dict)
            dictionaries = new_dictionaries
        return res


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        ("abcde", ["a", "bb", "acd", "ace"])
    ]

    for S, words in test_cases:
        print(solution.numMatchingSubseq(S, words))
