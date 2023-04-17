#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.ListNode
# Date: 2023/04/17
# Filename: ListNode

__author__ = "Yoshi Truong"
__date__ = "2023/04/17"


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def build(val):
        current = None
        for v in val[::-1]:
            current = ListNode(v, current)
        return current

    def to_tuple(self):
        node = self
        l = ()
        while node:
            l += (node.val,)
            node = node.next
        return l
