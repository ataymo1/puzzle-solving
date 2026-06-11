# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    # $ represents new layer
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
        nodes = data.split(".")
        # print(nodes)
        queue = deque()
        root = TreeNode(int(nodes[0]))
        queue.append(root)
        index = 0

        while queue:
            cur = queue.popleft()
            left, right = nodes[index + 1], nodes[index + 2]
            index += 2

            if left != "N":
                cur.left = TreeNode(int(left))
                queue.append(cur.left)
            if right != "N":
                cur.right = TreeNode(int(right))
                queue.append(cur.right)
        return root

            





        
        

        

