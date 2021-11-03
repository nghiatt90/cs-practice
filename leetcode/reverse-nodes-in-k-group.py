#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.reverse-nodes-in-k-group
# Date: 2021/11/03
# Filename: reverse-nodes-in-k-group

__author__ = "Yoshi Truong"
__date__ = "2021/11/03"

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_k(head, k):
    if not head:
        return False
    node = head
    for _ in range(k - 1):
        if not node.next:
            return False
        node = node.next

    node = head
    for _ in range(k - 1):
        t = node.next.next
        node.next.next = head
        head = node.next
        node.next = t
    return head


class Solution:
    """https://leetcode.com/problems/reverse-nodes-in-k-group/"""

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        tail = ListNode(0, head)
        node = head
        new_head = None
        while True:
            group_head = reverse_k(node, k)
            if not group_head:
                if not new_head:
                    return head
                else:
                    return new_head

            new_head = new_head or group_head
            tail.next = group_head
            tail = node
            node = node.next
