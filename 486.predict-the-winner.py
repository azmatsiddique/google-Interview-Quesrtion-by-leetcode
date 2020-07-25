#
# @lc app=leetcode id=486 lang=python3
#
# [486] Predict the Winner
#

# @lc code=start
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        dp = [0] * len(nums)
        for start in range(len(nums) - 1, -1, -1):
            dp[start] = nums[start]
            for end in range(start + 1, len(nums)):
                a = nums[start] - dp[end]
                b = nums[end] - dp[end - 1]
                dp[end] = max(a, b)
        return dp[len(nums) - 1] >= 0
# @lc code=end

