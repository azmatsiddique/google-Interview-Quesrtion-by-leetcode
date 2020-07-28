#
# @lc app=leetcode id=482 lang=python3
#
# [482] License Key Formatting
#

# @lc code=start
class Solution(object):
    def licenseKeyFormatting(self, S, K):

        c = S.upper().replace('-', '')
        h = 1 + (len(c)-1) % K
        return '-'.join(c[max(i-K,0):i] for i in range(h, len(c)+1, K))
        
# @lc code=end

