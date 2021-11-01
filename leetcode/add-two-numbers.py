# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        curr_node = root_node = ListNode(0)
        prev_node = None
        while l1 is not None or l2 is not None:
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0
            s = val1 + val2 + curr_node.val
            curr_node.val = s % 10
            curr_node.next = ListNode(s // 10)
            prev_node = curr_node
            curr_node = curr_node.next
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
        
        if curr_node.val == 0 and prev_node is not None:
            prev_node.next = None
        
        return root_node
