#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        
        l = len(height)
        if l == 0:
            return 0
        if l == 1:
            return 0
        maximum = max(height)
        lr = 0
        current = height[0]
        rain = 0
        while height[lr] < maximum:
            if current > height[lr]:
                rain += current - height[lr]
            else:
                current = height[lr]
            lr += 1
        
        er = l-1
        current = height[er]
        while height[er] < maximum:
            if current > height[er]:
                rain += current - height[er]
            else:
                current = height[er]
            er -= 1
        for i in range(lr,er+1):
            rain += maximum -height[i]

        return rain
        
        
        
# @lc code=end

