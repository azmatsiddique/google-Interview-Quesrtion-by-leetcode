#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        import heapq
        
        heap = []
        head = point = ListNode(0)
        
        for l in lists:
            while l:
                heapq.heappush(heap, l.val)
                l = l.next
        
        while heap:
            val = heapq.heappop(heap)
            point.next = ListNode(val)
            point = point.next
        point.next = None
        return head.next
        
# @lc code=end

