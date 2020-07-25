#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        if not nums:
            return nums
        i = len(nums) - 2
        while i >= 0:
            if nums[i] < nums[i+1]:
                break
            i -= 1
        if i != -1:            
            j = i + 1 
            while j < len(nums) and nums[j] > nums[i]:
                j += 1    
            j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        
# @lc code=end

