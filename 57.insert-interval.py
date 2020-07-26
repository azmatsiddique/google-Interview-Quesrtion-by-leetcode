#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start, end = newInterval[0], newInterval[1]
        left, right = [], []
        for a, b in intervals:
            if b < start:
                left.append([a, b])
            elif a > end:
                right.append([a, b])
            else:
                start = min(start, a)
                end = max(end, b)            
        return left + [[start, end]] + right
        
# @lc code=end

