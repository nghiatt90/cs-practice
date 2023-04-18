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


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)

    @staticmethod
    def to_string(root):
        if not root:
            return ''
        arr = [str(root.val)]
        nodes = [root]
        idx = 0
        while idx < len(nodes):
            if nodes[idx].left:
                nodes.append(nodes[idx].left)
                arr.append(str(nodes[idx].left.val))
            else:
                arr.append('null')
            if nodes[idx].right:
                nodes.append(nodes[idx].right)
                arr.append(str(nodes[idx].right.val))
            else:
                arr.append('null')
            idx += 1
        return ','.join(arr)

    @staticmethod
    def build_from_string(s, converter=None):
        converter = converter or Converter()
        s = s.strip()
        if s.startswith('['):
            s = s[1:]
        if s.endswith(']'):
            s = s[:-1]
        if not s:
            return None
        elements = [converter(x) for x in s.split(',')]
        root = TreeNode(elements[0])
        nodes = [root]
        idx = 0
        for i in range(1, len(elements), 2):
            lval = elements[i]
            rval = elements[i + 1] if i + 1 < len(elements) else None
            if lval is not None:
                nodes[idx].left = TreeNode(lval)
                nodes.append(nodes[idx].left)
            if rval is not None:
                nodes[idx].right = TreeNode(rval)
                nodes.append(nodes[idx].right)
            idx += 1
        return root


class Converter:
    def __init__(self, dtype=int, null_str='null', null_value=None):
        self.dtype = dtype
        self.null_str = null_str
        self.null_value = null_value

    def __call__(self, s):
        return self.null_value if s == self.null_str else self.dtype(s)
