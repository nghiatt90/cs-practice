#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.intersection-of-two-linked-lists
# Date: 2021/11/05
# Filename: intersection-of-two-linked-lists

__author__ = "Yoshi Truong"
__date__ = "2021/11/05"

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def length(head):
    cnt = 0
    while head:
        head = head.next
        cnt += 1
    return cnt


class Solution:
    """https://leetcode.com/problems/intersection-of-two-linked-lists/"""

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        la, lb = length(headA), length(headB)
        if not la * lb:
            return None

        diff = abs(la - lb)
        if la > lb:
            for _ in range(diff):
                headA = headA.next
        else:
            for _ in range(diff):
                headB = headB.next
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next

        return None
