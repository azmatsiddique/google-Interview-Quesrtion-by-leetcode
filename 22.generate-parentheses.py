#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return 0
        
        result = []
        self.helper(n, n, '', result)
        return result
    
    def helper(self, l, r, item, result):
        if r < l:
            return
        if l > 0:
            self.helper(l-1, r, item+'(', result)
            
        if r > 0:
            self.helper(l, r-1, item + ')', result)
            
        if r == 0 and l==0:
            result.append(item)
        
# @lc code=end

