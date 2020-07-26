#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        h = set()
        for n in nums:
            h.add(n)
        ans = 0
        while h:
            x = h.pop()
            count = 1
            a, b = x-1, x+1
            while a in h:
                count += 1
                h.remove(a)
                a -= 1
            while b in h:
                count += 1
                h.remove(b)
                b += 1
            ans = max(ans, count)
        return ans
# @lc code=end

