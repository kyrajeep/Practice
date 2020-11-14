# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#From the solution: make a subarray to store the length of each depth.
class Solution:
    def levelOrder(self, root):
        ans, level = [], [root]
        # start with the root
        while root and level:
            ans.append([node.val for node in level])
            LRpair = [(node.left, node.right) for node in level]
            level = [leaf for LR in LRpair for leaf in LR if leaf]
        return ans