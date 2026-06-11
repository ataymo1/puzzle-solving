# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        res = ""
        queue = deque()
        queue.append(root)

        while queue:
            cur = queue.popleft()
            if cur == None:
                res += "N"
                res += "."
            else:
                res += str(cur.val)
                res += "."

                if not cur.left:
                    queue.append(None)
                else:
                    queue.append(cur.left)

                if not cur.right:
                    queue.append(None)
                else:
                    queue.append(cur.right)
            
        
        return res

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None
        data = data.split(".")
        index = 0
        root = TreeNode(int(data[index]))

        queue = deque()
        queue.append(root)

        while queue:
            cur = queue.popleft()
            left, right = data[index + 1], data[index + 2]
            index += 2

            if left != "N":
                cur.left = TreeNode(int(left))
                queue.append(cur.left)
            if right != "N":
                cur.right = TreeNode(int(right))
                queue.append(cur.right)
        return root

            





        
        

        

