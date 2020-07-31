#
# @lc app=leetcode id=937 lang=python3
#
# [937] Reorder Data in Log Files
#

# @lc code=start
class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        let = [e for e in logs if e.split()[1:][0].isalpha()]
        dig = [e for e in logs if e.split()[1:][0].isdigit()]
        return sorted(let, key = lambda x: [x.split()[1:], x.split()[0]]) + dig
# @lc code=end

