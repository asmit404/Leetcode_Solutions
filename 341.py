"""
Title       : 341. Flatten Nested List Iterator
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 20 Oct 2023
Solved Using    : Python3
"""

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        def helper(nested_list):
            if not nested_list:
                return []

            pool = []
            for element in nested_list:
                if element.isInteger():
                    pool.append(element.getInteger())
                else:
                    pool.extend(helper(element.getList()))
            return pool

        self.flattened_list = helper(nestedList)
        self.index = 0

    def next(self) -> int:
        self.index += 1
        return self.flattened_list[self.index - 1]

    def hasNext(self) -> bool:
        if self.index >= len(self.flattened_list):
            return False
        return True

# Time Complexity  : O(n)
# Space Complexity : O(n)