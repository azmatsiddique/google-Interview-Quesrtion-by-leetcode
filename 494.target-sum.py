#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#

# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        # check if (S + sum(nums)) // 2 is int
        target, r = divmod(S + sum(nums), 2)
        if r != 0 or S > 1000:
            return 0
        
        dp = [0] * (target + 1)
        dp[0] = 1
        
        for n in nums:
            for total in range(target, n - 1, -1):
                dp[total] += dp[total - n]
                
        return dp[-1]
# @lc code=end

