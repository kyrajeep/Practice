def inorderTraversal1(self, root):
    res = []
    self.helper(root, res)
    return res
    
def helper(self, root, res):
    if root:
        self.helper(root.left, res)
        res.append(root.val)
        self.helper(root.right, res)
        #returns None
'''
Yuu's excellent comment:
The helper function looks correct.
Function argument can take two forms, value or reference.
If the argument is passed as a value, then it copies an object with same content. If the argument is passed as a reference, then it points to the same object.
In inorderTraversal1, res is passed as a reference at self.helper(root, res).
So when res.append(root.val) is executed inside helper function, it is appending to the original "res".
So when inorderTraversal1 returns res in the end of the function call, that 'res' is the object modified inside helper.
In python, functions can make some changes to arguments passed as a reference.
https://www.python-course.eu/passing_arguments.php
'''
 