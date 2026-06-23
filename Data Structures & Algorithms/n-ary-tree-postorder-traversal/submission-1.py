"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        if not root:
            return []

        cur = []

        for child in root.children:
            cur += self.postorder(child)
        
        cur.append(root.val)

        return cur
