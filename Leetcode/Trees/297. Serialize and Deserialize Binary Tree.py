from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec: # Preorder traversal (DFS)
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        # preorder traversal

        def dfs(node):
            if not node:
                res.append("N")
                return

            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(',')
        self.i = 0

        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None
            
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()
        
class Codec2: # Level order traversal (BFS)
    def serialize(self, root: TreeNode):
        res = []

        q = deque()
        q.append(root)
        
        while q:
            for i in range(len(q)):
                node:TreeNode = q.popleft()
                if node:
                    res.append(str(node.val))
                    q.append(node.left)
                    q.append(node.right)
                else:
                    res.append('N')
        return ','.join(res)
    
    def deserialize(self, data: str):
        if data == 'N':
            return
        
        data = data.split(',')
        root = TreeNode(data[0])

        q = deque()
        q.append(root)

        i = 1
        while q and i < len(data):
            node = q.popleft()

            if data[i] != 'N':
                node.left = TreeNode(int(data[i]))
                q.append(node.left)
            i += 1

            if i < len(data) and data[i] != 'N':
                node.right = TreeNode(int(data[i]))
                q.append(node.right)
            i += 1
        return root