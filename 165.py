"""
Title       : 165. Compare Version Numbers
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 3 May 2024
"""

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split(".")
        version2 = version2.split(".")
        for i in range(max(len(version1), len(version2))):
            rev1 = int(version1[i]) if i < len(version1) else 0
            rev2 = int(version2[i]) if i < len(version2) else 0
            if rev1 < rev2: return -1
            elif rev1 > rev2: return 1
        return 0

# Time Complexity  : O(n)
# Space Complexity : O(n)