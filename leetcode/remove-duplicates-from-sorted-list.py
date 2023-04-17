#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.remove-duplicates-from-sorted-list
# Date: 2023/04/17
# Filename: remove-duplicates-from-sorted-list

__author__ = "Yoshi Truong"
__date__ = "2023/04/17"

from typing import Optional

from leetcode.ListNode import ListNode


# https://leetcode.com/problems/remove-duplicates-from-sorted-list/


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        while node and node.next:
            if node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next
        return head


if __name__ == '__main__':
    assert Solution().deleteDuplicates(ListNode.build([1, 1, 2])).to_tuple() == (1, 2)
    assert Solution().deleteDuplicates(ListNode.build([1, 1, 2, 3, 3])).to_tuple() == (1, 2, 3)
