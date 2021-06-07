# https://leetcode.com/problems/merge-k-sorted-lists
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        root = ListNode()
        current = root
        
        while True:
            min_val, min_id = 999999, -1
            for i, l in enumerate(lists):
                if l and l.val < min_val:
                    min_val = l.val
                    min_id = i
            if min_id == -1:
                break
            
            current.next = lists[min_id]
            lists[min_id] = lists[min_id].next
            current = current.next
        
        return root.next
