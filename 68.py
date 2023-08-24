"""
Title       : 68. Text Justification
Difficulty  : Hard
Author      : Asmit Singh
Solved On   : 24 Aug 2023
Solved Using    : Python3
"""

class Solution:
    def fullJustify(self, words, maxWidth):
        res, cur, num = [], [], 0
        for words in words:
            if num + len(words) + len(cur) > maxWidth:
                for i in range(maxWidth - num):
                    cur[i%(len(cur)-1 or 1)] += ' '
                res.append(''.join(cur))
                cur, num = [], 0
            cur += [words]
            num += len(words)
        return res + [' '.join(cur).ljust(maxWidth)]

# Time Complexity  : O(n)
# Space Complexity : O(n)