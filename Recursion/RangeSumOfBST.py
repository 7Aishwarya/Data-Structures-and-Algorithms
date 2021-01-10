# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.sum1 = 0
        
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        if root == None:
            return 0
        if root.val >= low and root.val <= high:
            self.sum1 += root.val
        if root.val > low:
            self.rangeSumBST(root.left, low, high)
        if root.val < high:
            self.rangeSumBST(root.right, low, high)
        return self.sum1
        