class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
        
        
def helper(node, minValue = float('-inf'), maxValue = float('inf')):
    if not node:
        return True
    val = node.val
    if val <= minValue or val >= maxValue:
        return True      
    if not helper(node.right, val, maxValue):
        return False
    if not helper(node.left, minValue, val):
        return False
    
    return True  


def isValidBST(root):
    return helper(root)



root1 = TreeNode(2)
root1.left = TreeNode(1)
root1.right = TreeNode(3)

print(isValidBST(root1))
