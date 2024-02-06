"""
Title       : 49. Group Anagrams
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 06 Feb 2024
"""

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        hmap = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            hmap[tuple(count)].append(word)
        return list(hmap.values())

# Time Complexity  : O(n * k)
# Space Complexity : O(n * k)