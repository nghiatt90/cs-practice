#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.linked-list-cycle
# Date: 2021/11/05
# Filename: linked-list-cycle

__author__ = "Yoshi Truong"
__date__ = "2021/11/05"

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """https://leetcode.com/problems/linked-list-cycle/"""

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        p1 = head
        p2 = head
        while True:
            if not p1.next or not p2.next:
                return False
            p1 = p1.next
            if not p1.next:
                return False
            p1 = p1.next
            p2 = p2.next
            if p1 == p2:
                return True
