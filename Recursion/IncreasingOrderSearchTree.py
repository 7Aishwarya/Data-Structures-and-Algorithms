# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.temp1 = TreeNode(0)
        self.temp2 = self.temp1
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return
        self.increasingBST(root.left)
        self.temp1.right = TreeNode(root.val)
        self.temp1 = self.temp1.right
        self.increasingBST(root.right)
        return self.temp2.right
        
        