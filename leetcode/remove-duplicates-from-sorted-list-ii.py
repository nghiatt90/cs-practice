#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.remove-duplicates-from-sorted-list-ii
# Date: 2023/04/17
# Filename: remove-duplicates-from-sorted-list-ii

__author__ = "Yoshi Truong"
__date__ = "2023/04/17"


from typing import Optional

from leetcode.ListNode import ListNode


# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        node = head
        prev = ListNode(-999, head)
        while node:
            current = node.val
            if node.next and node.next.val == current:
                # duplicate
                while node.next and node.next.val == current:
                    node.next = node.next.next
                prev.next = node.next
                if prev.val == -999:
                    # head moves
                    head = prev.next
            else:
                # no duplicate
                prev = node
            node = node.next

        return head


if __name__ == '__main__':
    assert Solution().deleteDuplicates(ListNode.build([1,2,3,3,4,4,5])).to_tuple() == (1, 2, 5)
    assert Solution().deleteDuplicates(ListNode.build([1,1,1,2,3])).to_tuple() == (2, 3)
    assert Solution().deleteDuplicates(ListNode.build([1, 1])) is None
    assert Solution().deleteDuplicates(ListNode.build([1])).to_tuple() == (1,)
