#
# @lc app=leetcode id=652 lang=python3
#
# [652] Find Duplicate Subtrees
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        counter = collections.Counter()
        res = [] 
        def dfs(node):
            if not node:
                return ' '
            serialize = str(node.val) + ',' + dfs(node.left) + ',' + dfs(node.right)
            if counter[serialize] == 1:
                res.append(node)
            counter[serialize] += 1    
            return serialize
        dfs(root)
        return res 
        
# @lc code=end

