# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        else:
            if p.val == q.val:
            # check if the left and right children are both the same at the same time
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            else:
            # false if values are different
                return False
