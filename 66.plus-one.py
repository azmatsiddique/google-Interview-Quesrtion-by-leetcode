#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string = ''
        for item in digits:
            string += str(item)
        sum = int(string) + 1
        lst = []
        for i in str(sum):
            lst.append(i)
        return lst
# @lc code=end

