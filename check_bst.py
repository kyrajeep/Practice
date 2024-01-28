# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):
            if not node:
                return True
            if not (node.val > left and node.val < right):
                return False
            # For the left child, the right boundary is updated whereas the left 
            # boundary remains the same. The left boundary does not change as we travel one depth down.
            return valid(node.left, left, node.val) and valid(node.right, node.val, right) # because of the and clause it will return false if any one is false
        # because there is no upper or lower bound on the root, we do not assign them in the beginnign.
        return valid(root, float(-inf), float(inf))
        
