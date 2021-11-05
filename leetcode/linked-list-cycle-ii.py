#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.linked-list-cycle-ii
# Date: 2021/11/05
# Filename: linked-list-cycle-ii

__author__ = "Yoshi Truong"
__date__ = "2021/11/05"

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """https://leetcode.com/problems/linked-list-cycle-ii/"""

    def detectCycle(self, head: ListNode) -> Optional[ListNode]:
        if not head:
            return None
        p1 = head
        p2 = head
        entry = head
        while True:
            if not p1.next or not p2.next:
                return None
            p1 = p1.next
            if not p1.next:
                return None
            p1 = p1.next
            p2 = p2.next
            if p1 == p2:
                while p2 != entry:
                    p2 = p2.next
                    entry = entry.next
                return entry
