"""
Title       : 150. Evaluate Reverse Polish Notation
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 30 Jan 2024
"""

from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {"+": lambda a, b: a + b, 
               "-": lambda a, b: a - b, 
               "/": lambda a, b: int(a / b), 
               "*": lambda a, b: a * b}
        pool = []
        for token in tokens:
            if token in ops:
                num2 = pool.pop()
                num1 = pool.pop()
                op = ops[token]
                pool.append(op(num1, num2))
            else:
                pool.append(int(token))
        return pool.pop()

# Time Complexity  : O(n)
# Space Complexity : O(n)