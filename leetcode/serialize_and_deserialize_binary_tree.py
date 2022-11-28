class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return 'N'
        return f"{root.val},{self.serialize(root.left)},{self.serialize(root.right)}"

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        node_vals = data.split(',')
        idx = [0]

        def recurse():
            if node_vals[idx[0]] == 'N':
                idx[0] += 1
                return None
            root = TreeNode(node_vals[idx[0]])
            idx[0] += 1
            root.left = recurse()
            root.right = recurse()

            return root
        
        return recurse()