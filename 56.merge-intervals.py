    #
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        
        rep=[]
        k=0
        while k<len(intervals):
            l=intervals[k][0]
            r=intervals[k][1]
            k+=1
            while k<len(intervals):
                if intervals[k][0]>r:
                    break
                else:
                    r=max(intervals[k][1],r)
                    k+=1
            rep.append([l,r])
        return rep
        
# @lc code=end

