# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.min1 = 100
        self.prev = None
        self.arr = []
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return
        self.minDiffInBST(root.left)
        
        if self.prev:
            self.min1 = min(self.min1, abs(root.val - self.prev))
        self.prev = root.val
        
        self.minDiffInBST(root.right)
        
        return self.min1