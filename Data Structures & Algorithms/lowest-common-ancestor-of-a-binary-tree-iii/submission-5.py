"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        temp_p = p
        temp_q = q
        while temp_p is not temp_q:
            if temp_p.parent is None:
                temp_p = q
            else:
                temp_p = temp_p.parent
            if temp_q.parent is None:
                temp_q = p
            else:
                temp_q = temp_q.parent
        return temp_p
            



