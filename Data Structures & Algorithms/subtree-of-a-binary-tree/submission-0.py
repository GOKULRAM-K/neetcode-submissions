# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSub(val, subRoot):
            if not val and not subRoot:
                return True

            if not val or not subRoot:
                return False

            if val.val!=subRoot.val:
                return False

            return isSub(val.left, subRoot.left) and isSub(val.right, subRoot.right)
        def dfs(root):
            if not root:
                return False

            if root.val == subRoot.val:
                if isSub(root, subRoot):
                    return True
            return dfs(root.left) or dfs(root.right)

        return dfs(root)