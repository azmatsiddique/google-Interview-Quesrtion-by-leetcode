#
# @lc app=leetcode id=657 lang=python3
#
# [657] Robot Return to Origin
#

# @lc code=start
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        count=0
        count1=0
        for i in moves:
            if i=='L':
                count+=1              
            elif i=='R':
                count-=1          
            if i=='U':
                count1+=1      
            elif i=='D':
                count1-=1
        if count==0 and count1==0:
            return True
        
# @lc code=end

